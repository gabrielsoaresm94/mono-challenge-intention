import axiosProvider from '../../../../../shared/providers/proxy-provider/implementations/axios-provider';

enum HTTPMethod {
  GET = 'get',
  POST = 'post',
  PUT = 'put',
  DELETE = 'delete',
  PATCH = 'patch',
}

const URL = 'https://fakestoreapi.com';

class ProductRepository {
  public static async list() {
    const GET = 'get' as HTTPMethod;
    const productsResponse = await axiosProvider(GET, `${URL}/products`);

    if (!productsResponse) {
      return productsResponse;
    }

    const productsListed = productsResponse.data;

    return productsListed;
  }
}

export default ProductRepository;
