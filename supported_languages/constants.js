import fs from 'fs';

export const SUPPORTED_LANGUAGES = JSON.parse(fs.readFileSync('./supported_languages/supported_languages.json', 'utf8'));


export const COUNTRIES = JSON.parse(fs.readFileSync('./supported_languages/countries.json', 'utf8'));

console.log(SUPPORTED_LANGUAGES)
console.log(COUNTRIES)