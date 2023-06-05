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

  public static async find(productId: number) {
    const GET = 'get' as HTTPMethod;
    const productResponse = await axiosProvider(GET, `${URL}/products/${productId}`);

    if (!productResponse) {
      return productResponse;
    }

    const productFound = productResponse.data;

    return productFound;
  }
}

export default ProductRepository;
