import axios, { AxiosResponse } from 'axios';

export enum HTTPMethod {
  GET = 'get',
  POST = 'post',
  PUT = 'put',
  DELETE = 'delete',
  PATCH = 'patch',
}

export async function axiosProvider(
  httpMethod: HTTPMethod,
  url: string,
  queryParams?: Object,
  body?: Object
): Promise<AxiosResponse<Object> | undefined> {
  try {
    let response = undefined;

    switch (httpMethod) {
      case HTTPMethod.GET:
        response = await axios.get(url, {
          params: !!queryParams ? queryParams : {},
        });
        break;
      case HTTPMethod.POST:
        response = await axios.post(url, body, {
          headers: {
            'Content-Type': 'application/json'
          }}
        );
        break;
      case HTTPMethod.PUT:
        response = await axios.put(url, body);
        break;
      case HTTPMethod.DELETE:
        response = await axios.delete(url);
        break;
      case HTTPMethod.PATCH:
        response = await axios.patch(url, body);
        break;
      default:
        response = undefined;
    }

    return response;
  } catch (error: any) {
    console.error(error);
    throw new Error (error);
  }
}

