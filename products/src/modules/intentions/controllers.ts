import { Router, Request, Response } from 'express';
import UpdateIntention from './services/update-intention';
import FindProduct from '../products/services/found-products';
import { IProduct, IntentionStatus } from './dtos';
import { IResponse } from '../../shared/dtos';

const intentionsRouter = Router();

/**
 * @swagger
 * /intentions/<intention_id>:
 *   put:
 *     summary: Seleciona produtos e atualiza intenção.
 *     description: Seleciona produtos dá intenção de compra e atualiza status.
 *     tags:
 *       - Intentions
 *     responses:
 *       200:
 *         description: Success
 */
intentionsRouter.put(
  '/',
  async (req: Request, res: Response): Promise<Response> => {
    const intentionId: Number = req.body.intention_id;
    const productsIds: Array<Number> =  req.body.products_ids;

    if (!intentionId) {}

    if (!productsIds || (productsIds && productsIds.length <= 0)) {}

    const products: Array<IProduct> = []
    for (const productId of productsIds) {
      const product = await FindProduct.execute(productId);
      if (!product) {
        continue;
      }
      products.push(product);
    }

    const intentionUpdated = await UpdateIntention.execute(
      intentionId,
      "SELECIONADO" as IntentionStatus,
      products
    );

    if (!intentionUpdated) {
      return res.status(400).json({
        message: 'Problemas para selecionar produtos para a intenção de compra.',
        status: false,
      });
    }

    return res.status(200).json({
      message: 'Produtos selecionados para a intenção de compra com sucesso!',
      status: true,
    });
  }
);