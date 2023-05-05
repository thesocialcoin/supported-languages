import { COUNTRIES } from "./constants.js";
import { getSupportedLanguages as getSupportedLangs } from "./languages.js";


export function getAvailableCountries(){
    const languages = getSupportedLangs()
    return Object.keys(COUNTRIES).filter(k =>
        COUNTRIES[k]["languages"].some(lang => languages.includes(lang))
      );
}


export function getCountries() {
    return Object.keys(COUNTRIES)
}


export function getCountry(countryCode) {
    return COUNTRIES[countryCode] || {}
}


export function getLanguages(countryCode) {
    return COUNTRIES[countryCode] ? COUNTRIES[countryCode]["languages"] : {}
}


export function getSupportedLanguages(countryCode) {
    const languages = getSupportedLangs()
    const countryLanguages = getLanguages(countryCode)
    return Object.keys(countryLanguages).length !== 0 ? 
            getLanguages(countryCode).filter(lang => languages.includes(lang)) : {}
}
