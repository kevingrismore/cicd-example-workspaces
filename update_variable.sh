curl -X PATCH "$PREFECT_API_URL/variables/name/$VARIABLE_NAME" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $PREFECT_API_KEY" \
  -d '{"name": "'"$VARIABLE_NAME"'", "value": "'"$VARIABLE_VALUE"'", "tags": []}'