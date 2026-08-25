import {request} from "./api";
import {getToken} from "./authService";


export async function getProfile(){

return request(
"/profile/me",
{
method:"GET",
token:getToken() ?? undefined
}
);

}



export async function updateProfile(
data:any
){

return request(
"/profile/me",
{

method:"PATCH",

token:getToken() ?? undefined,


headers:{
"Content-Type":"application/json"
},

body:
JSON.stringify(data)

}
);

}