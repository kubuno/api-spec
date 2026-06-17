#!/usr/bin/env bash
# Regenerate the mobile OpenAPI spec and the Swift/Kotlin clients.
#   bash generate.sh [CORE_URL]    # default: http://localhost:8080
set -euo pipefail
cd "$(dirname "$0")"

CORE="${1:-http://localhost:8080}"
GEN="npx --yes @openapitools/openapi-generator-cli"

echo "→ fetching core spec from $CORE"
curl -sf "$CORE/api/v1/openapi.json" -o openapi.core.json

echo "→ building mobile spec"
python3 build_spec.py openapi.core.json openapi.json

echo "→ generating Swift client (clients/swift)"
rm -rf clients/swift
$GEN generate -i openapi.json -g swift5 -o clients/swift \
  --additional-properties=projectName=KubunoAPI,responseAs=AsyncAwait,useSPMFileStructure=true \
  >/dev/null

echo "→ generating Kotlin client (clients/kotlin)"
rm -rf clients/kotlin
$GEN generate -i openapi.json -g kotlin -o clients/kotlin \
  --additional-properties=packageName=com.kubuno.api,library=jvm-okhttp4,serializationLibrary=kotlinx_serialization \
  >/dev/null

echo "✓ done — clients in clients/swift and clients/kotlin"
