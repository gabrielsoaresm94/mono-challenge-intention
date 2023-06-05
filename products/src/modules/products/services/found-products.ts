import ProductRepository from '../infra/fake-store-api/repositories/product-repository';

class FoundProduct {
  public static async execute(productId: number): Promise<Object | undefined> {
    const productFound = await ProductRepository.find(productId);
    return productFound;
  }
}

export default FoundProduct;
