import { axiosProvider, HTTPMethod } from '../../../../../shared/providers/proxy-provider/implementations/axios-provider';
import { IProduct } from '../../../../intentions/dtos';

const URL = 'https://fakestoreapi.com';

class ProductRepository {
  public static async list(): Promise<Array<IProduct> | undefined> {
    const GET = 'get' as HTTPMethod;
    const productsResponse = await axiosProvider(GET, `${URL}/products`);

    if (!productsResponse) {
      return productsResponse;
    }

    const productsListed = productsResponse.data as Array<IProduct>;

    return productsListed;
  }

  public static async find(productId: Number): Promise<IProduct | undefined> {
    const GET = 'get' as HTTPMethod;
    const productResponse = await axiosProvider(GET, `${URL}/products/${productId}`);

    if (!productResponse) {
      return productResponse;
    }

    const productFound = productResponse.data as IProduct;

    return productFound;
  }
}

export default ProductRepository;
