#!/usr/bin/env python3
"""Build the Kubuno *mobile* OpenAPI spec.

Starts from the live core spec (auth / me / modules, generated from code via
utoipa) and augments it with the mobile-relevant surface that lives in the
drive module and the push endpoints — documented here from the actual handlers.
Output: openapi.json (OpenAPI 3.1), the input for client generation.
"""
import json
import sys

src = sys.argv[1] if len(sys.argv) > 1 else "openapi.core.json"
out = sys.argv[2] if len(sys.argv) > 2 else "openapi.json"

spec = json.load(open(src))

spec["info"]["title"] = "Kubuno Mobile API"
# OpenAPI 3.1 requires an SPDX identifier (or url) on the license.
spec["info"]["license"] = {"name": "AGPL-3.0-or-later", "identifier": "AGPL-3.0-or-later"}
spec["info"]["description"] = (
    "API surface consumed by the Kubuno native mobile apps (iOS/Android): "
    "native auth, drive delta-sync, files/folders and push notifications. "
    "Core auth/me paths are generated from the server; drive and push paths "
    "are documented from their handlers."
)

sec = [{"bearer": []}]
paths = spec["paths"]
schemas = spec["components"]["schemas"]

# ── Schemas ────────────────────────────────────────────────────────────────
schemas["DriveChange"] = {
    "type": "object",
    "description": "One change in the drive delta. `kind` discriminates the shape.",
    "required": ["kind", "change_seq"],
    "properties": {
        "kind": {"type": "string", "enum": ["file", "folder", "deleted"]},
        "id": {"type": "string", "format": "uuid"},
        "name": {"type": "string"},
        "folder_id": {"type": "string", "format": "uuid", "nullable": True},
        "parent_id": {"type": "string", "format": "uuid", "nullable": True},
        "path": {"type": "string", "description": "Materialized folder path (folders)."},
        "etag": {"type": "string", "nullable": True, "description": "Content hash (files)."},
        "size": {"type": "integer", "format": "int64"},
        "mime_type": {"type": "string"},
        "trashed": {"type": "boolean"},
        "target": {"type": "string", "enum": ["file", "folder"], "description": "Deleted item kind."},
        "deleted_at": {"type": "string", "format": "date-time"},
        "change_seq": {"type": "integer", "format": "int64"},
    },
}
schemas["DriveDelta"] = {
    "type": "object",
    "required": ["changes", "cursor", "has_more"],
    "properties": {
        "changes": {"type": "array", "items": {"$ref": "#/components/schemas/DriveChange"}},
        "cursor": {"type": "integer", "format": "int64"},
        "has_more": {"type": "boolean"},
    },
}
schemas["DriveFolder"] = {
    "type": "object",
    "properties": {
        "id": {"type": "string", "format": "uuid"},
        "name": {"type": "string"},
        "parent_id": {"type": "string", "format": "uuid", "nullable": True},
        "path": {"type": "string"},
    },
}
schemas["CreateFolderDto"] = {
    "type": "object",
    "required": ["name"],
    "properties": {
        "parent_id": {"type": "string", "format": "uuid", "nullable": True},
        "name": {"type": "string"},
    },
}
schemas["RegisterDeviceDto"] = {
    "type": "object",
    "required": ["provider", "device_token"],
    "properties": {
        "provider": {"type": "string", "enum": ["unifiedpush", "apns", "fcm"]},
        "device_token": {"type": "string", "description": "Endpoint URL (unifiedpush) or push token."},
        "app_id": {"type": "string"},
        "locale": {"type": "string"},
    },
}
schemas["SetPreferenceDto"] = {
    "type": "object",
    "required": ["enabled"],
    "properties": {
        "module_id": {"type": "string", "description": "'*' = all modules."},
        "event_type": {"type": "string", "description": "'*' = all events."},
        "enabled": {"type": "boolean"},
    },
}

# ── Reusable header parameters ──────────────────────────────────────────────
IDEMPOTENCY = {
    "name": "Idempotency-Key", "in": "header", "required": False,
    "schema": {"type": "string"},
    "description": "Stable key so a replayed mutation is not applied twice.",
}
IF_MATCH = {
    "name": "If-Match", "in": "header", "required": False,
    "schema": {"type": "string"},
    "description": "Expected etag; mismatch returns 412 (conflict).",
}

# ── Push paths ──────────────────────────────────────────────────────────────
paths["/api/v1/me/push/devices"] = {
    "post": {
        "tags": ["push"], "summary": "Register (or refresh) a push device.",
        "security": sec,
        "requestBody": {"required": True, "content": {"application/json": {
            "schema": {"$ref": "#/components/schemas/RegisterDeviceDto"}}}},
        "responses": {"201": {"description": "Registered (returns the device id)."},
                       "422": {"description": "Invalid provider/token."}},
    }
}
paths["/api/v1/me/push/devices/{id}"] = {
    "delete": {
        "tags": ["push"], "summary": "Unregister a push device.", "security": sec,
        "parameters": [{"name": "id", "in": "path", "required": True,
                        "schema": {"type": "string", "format": "uuid"}}],
        "responses": {"200": {"description": "Removed."}, "404": {"description": "Unknown device."}},
    }
}
paths["/api/v1/me/push/preferences"] = {
    "get": {"tags": ["push"], "summary": "List push opt-out preferences.", "security": sec,
            "responses": {"200": {"description": "Preferences list."}}},
    "patch": {"tags": ["push"], "summary": "Upsert one push preference.", "security": sec,
              "requestBody": {"required": True, "content": {"application/json": {
                  "schema": {"$ref": "#/components/schemas/SetPreferenceDto"}}}},
              "responses": {"200": {"description": "Saved."}}},
}

# ── Drive paths (proxied as /api/v1/drive/...) ──────────────────────────────
paths["/api/v1/drive/sync/delta"] = {
    "get": {
        "tags": ["drive-sync"], "summary": "Changes since a cursor (delta sync).",
        "security": sec,
        "parameters": [
            {"name": "cursor", "in": "query", "schema": {"type": "integer", "format": "int64", "default": 0},
             "description": "Last change_seq seen (0 = full snapshot)."},
            {"name": "limit", "in": "query", "schema": {"type": "integer", "default": 500}},
        ],
        "responses": {"200": {"description": "Delta page.", "content": {"application/json": {
            "schema": {"$ref": "#/components/schemas/DriveDelta"}}}}},
    }
}
paths["/api/v1/drive/sync/file/{id}/content"] = {
    "put": {
        "tags": ["drive-sync"], "summary": "Replace a file's content (conflict-safe).",
        "security": sec,
        "parameters": [
            {"name": "id", "in": "path", "required": True, "schema": {"type": "string", "format": "uuid"}},
            IF_MATCH, IDEMPOTENCY,
        ],
        "requestBody": {"required": True, "content": {"application/octet-stream": {
            "schema": {"type": "string", "format": "binary"}}}},
        "responses": {"200": {"description": "Updated (returns new etag)."},
                       "412": {"description": "Conflict: server content changed."}},
    }
}
paths["/api/v1/drive/upload"] = {
    "post": {
        "tags": ["drive"], "summary": "Upload a new file (multipart).", "security": sec,
        "parameters": [IDEMPOTENCY],
        "requestBody": {"required": True, "content": {"multipart/form-data": {"schema": {
            "type": "object",
            "properties": {
                "file": {"type": "string", "format": "binary"},
                "folder_id": {"type": "string", "format": "uuid"},
            }, "required": ["file"]}}}},
        "responses": {"200": {"description": "Created file."}},
    }
}
paths["/api/v1/drive/folders"] = {
    "post": {
        "tags": ["drive"], "summary": "Create a folder.", "security": sec,
        "parameters": [IDEMPOTENCY],
        "requestBody": {"required": True, "content": {"application/json": {
            "schema": {"$ref": "#/components/schemas/CreateFolderDto"}}}},
        "responses": {"200": {"description": "Created folder.", "content": {"application/json": {
            "schema": {"type": "object", "properties": {
                "folder": {"$ref": "#/components/schemas/DriveFolder"}}}}}}},
    }
}
paths["/api/v1/drive/{id}/download"] = {
    "get": {
        "tags": ["drive"], "summary": "Download a file's content.", "security": sec,
        "parameters": [{"name": "id", "in": "path", "required": True,
                        "schema": {"type": "string", "format": "uuid"}}],
        "responses": {"200": {"description": "File bytes.", "content": {"application/octet-stream": {
            "schema": {"type": "string", "format": "binary"}}}}},
    }
}
paths["/api/v1/drive/{id}/trash"] = {
    "post": {
        "tags": ["drive"], "summary": "Move a file to trash.", "security": sec,
        "parameters": [{"name": "id", "in": "path", "required": True,
                        "schema": {"type": "string", "format": "uuid"}}, IDEMPOTENCY],
        "responses": {"200": {"description": "Trashed."}},
    }
}

# ── Tags ────────────────────────────────────────────────────────────────────
spec.setdefault("tags", [])
existing = {t["name"] for t in spec["tags"]}
for name, desc in [
    ("drive", "Files & folders"),
    ("drive-sync", "Delta synchronisation"),
    ("push", "Push notifications"),
]:
    if name not in existing:
        spec["tags"].append({"name": name, "description": desc})

json.dump(spec, open(out, "w"), indent=2, ensure_ascii=False)
print(f"écrit {out} : {len(spec['paths'])} paths, {len(spec['components']['schemas'])} schemas")
