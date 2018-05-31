import axios from 'axios'

export const http = axios.create({
    baseURL: 'https://www.pvargapi.win'//'https://www.pvargapi.win/',
})

export function tokenedAxios(token) {
    return axios.create({
        baseURL: 'https://www.pvargapi.win',//'https://www.pvargapi.win/',
        headers: {
            Authorization: 'Token ' + token,
            'Access-Control-Allow-Origin': '*'
        }
    })
}