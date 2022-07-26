package main

import (
	"bytes"
	"crypto/rsa"
	"crypto/x509"
	"encoding/base64"
	"encoding/json"
	"encoding/pem"
	"fmt"
	"log"
	"math/big"
)

var js1 = `{"alg":"RS256","e":"AQAB","n":"ok6rvXu95337IxsDXrKzlIqw_I_zPDG8JyEw2CTOtNMoDi1QzpXQVMGj2snNEmvNYaCTmFf51I-EDgeFLLexr40jzBXlg72quV4aw4yiNuxkigW0gMA92OmaT2jMRIdDZM8mVokoxyPfLub2YnXHFq0XuUUgkX_TlutVhgGbyPN0M12teYZtMYo2AUzIRggONhHvnibHP0CPWDjCwSfp3On1Recn4DPxbn3DuGslF2myalmCtkujNcrhHLhwYPP-yZFb8e0XSNTcQvXaQxAqmnWH6NXcOtaeWMQe43PNTAyNinhndgI8ozG3Hz-1NzHssDH_yk6UYFSszhDbWAzyqw","kid":"wyMwK4A6CL9Qw11uofVeyQ119XyX-xykymkkXygZ5OM","kty":"RSA","use":"sig"}`
var js = `{"alg":"RS256","e":"AQAB","n":"pNiQA5UVxG3C099ROlwRIR7TUyCKdMyomSTAi9cZngpvdeVCbl5YnF4vWm_7klMxdJXanAVHB1mpHAnIfDCAZIWCWmI3C3F8JUPKvtR6m7gFd2sV5Y9tQWbMiXLgGct4No_pdiqdQvp50X4jQw0LWIrHhwN2z965TfsKDNcT-oQN2cA9OvuEgsDjJEoZK-FO9Mgkb44AvPpH2Rf6tHOH9PgABlfWLlSaB4QWkIncnhc1An0Mh1XNA4vKXz-wF1Mj70iX9Dnn0UZmFw8dHyENCSUQNl2by25EGh4RLG2GJRhR6aZSodKTXFG4n-p6SaOC2mL3c-Jlrzlz2_BrI85Ezw","kty":"RSA","use":"sig"}`
func main() {
	jwk := map[string]string{}
	json.Unmarshal([]byte(js), &jwk)
	
	fmt.Println(jwk["kty"])
	if jwk["kty"] != "RSA" {
		log.Fatal("invalid key type:", jwk["kty"])
	}

	// decode the base64 bytes for n
	nb, err := base64.RawURLEncoding.DecodeString(jwk["n"])
	if err != nil {
		log.Fatal(err)
	}
	
	fmt.Println(new(big.Int).SetBytes(nb))

	e := 0
	// The default exponent is usually 65537, so just compare the
	// base64 for [1,0,1] or [0,1,0,1]
	if jwk["e"] == "AQAB" || jwk["e"] == "AAEAAQ" {
		e = 65537
	} else {
		// need to decode "e" as a big-endian int
		log.Fatal("need to deocde e:", jwk["e"])
	}

	pk := &rsa.PublicKey{
		N: new(big.Int).SetBytes(nb),
		E: e,
	}
	

	der, err := x509.MarshalPKIXPublicKey(pk)
	if err != nil {
		log.Fatal(err)
	}

	block := &pem.Block{
		Type:  "RSA PUBLIC KEY",
		Bytes: der,
	}

	var out bytes.Buffer
	pem.Encode(&out, block)
	fmt.Println(out.String())
}
