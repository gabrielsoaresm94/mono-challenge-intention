import ProductRepository from '../infra/fake-store-api/repositories/product-repository';

class ListProducts {
  public static async execute(): Promise<Object | undefined> {
    const productsListed = await ProductRepository.list();
    return productsListed;
  }
}

export default ListProducts;
