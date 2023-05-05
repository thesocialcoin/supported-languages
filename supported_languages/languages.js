import { SUPPORTED_LANGUAGES } from "./constants.js";

 export function getSupportedLanguages() {
    return Object.keys(SUPPORTED_LANGUAGES).filter(k =>
        Object.values(SUPPORTED_LANGUAGES[k]["webhooks"]).every(Boolean)
      );
}

 export function getLanguages() {
    return Object.keys(SUPPORTED_LANGUAGES)
}

 export function getLanguage(languageCode) {
    return SUPPORTED_LANGUAGES[languageCode] || {}
}


console.log(getSupportedLanguages())
console.log(getLanguages())
console.log(getLanguage("es"))