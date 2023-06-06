import { IProduct } from '../../intentions/dtos';
import ProductRepository from '../infra/fake-store-api/repositories/product-repository';

class FindProduct {
  public static async execute(productId: Number): Promise<IProduct | undefined> {
    const productFound = await ProductRepository.find(productId);
    return productFound;
  }
}

export default FindProduct;
