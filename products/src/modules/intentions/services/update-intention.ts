import { axiosProvider, HTTPMethod } from "../../../shared/providers/proxy-provider/implementations/axios-provider";
import { IIntentionProduct, IntentionStatus, IProduct } from "../dtos";

class UpdateIntention {
  public static async execute(
    intentionId: Number,
    intentionStatus: IntentionStatus,
    products: Array<IProduct>
  ): Promise<Object | undefined> {
    const intentionProducts: Array<IIntentionProduct> = [];

    for (const product of products) {
      const intentionProduct = {
        product_id: product.id,
        title: product.title,
        price: product.price,
        category: product.category,
        description: product.description,
        image: product.image,
        quantity: null,
        intention_id: intentionId,
      };
      intentionProducts.push(intentionProduct);
    }

    const intentionRequestBody = {
      intention_status: intentionStatus,
      intention_products: intentionProducts,
    };
    const PATCH = 'patch' as HTTPMethod;
    const url = 'http://intentions-service:5000/v1/intentions/'
    const intentionUpdated = await axiosProvider(PATCH, `${url}/${intentionId}/`, intentionRequestBody);

    if (!intentionUpdated) {
      return intentionUpdated;
    }

    const intentionReturn = intentionUpdated.data;

    return intentionReturn;
  }
}

export default UpdateIntention;
