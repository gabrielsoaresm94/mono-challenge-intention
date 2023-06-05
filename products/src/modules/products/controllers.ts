import { Router, Request, Response } from 'express';
import ListProducts from './services/list-products';
import FoundProduct from './services/found-products';

const productsRouter = Router();

/**
 * @swagger
 * /products/:
 *   get:
 *     summary: Retorna a lista de produtos.
 *     description: Lista de produtos retornada com sucesso.
 *     tags:
 *       - Products
 *     responses:
 *       200:
 *         description: Success
 */
productsRouter.get(
  '/',
  async (req: Request, res: Response): Promise<Response> => {

    const productsListed = await ListProducts.execute();

    if (!productsListed) {
      return res.status(400).json({
        message: 'Problemas para listar produtos.',
      });
    }

    return res.status(200).json({
      message: 'Produtos listados com sucesso!',
      data: productsListed,
    });
  }
);

/**
 * @swagger
 * /products/{product_id}:
 *   get:
 *     summary: Retorna produto.
 *     description: Produto retornado com sucesso.
 *     tags:
 *       - Products
 *     parameters:
 *        - name: product_id
 *          in: path
 *          description: "Id do produto"
 *          required: true
 *          type: string
 *     responses:
 *       200:
 *         description: Success
 */
productsRouter.get(
  '/:product_id',
  async (req: Request, res: Response): Promise<Response> => {
    const productId = parseInt(req.params.product_id);

    if (!productId) {
      return res.status(400).json({
        message: 'O campo "product_id" deve ser do tipo inteiro.',
      });
    }

    const productsListed = await FoundProduct.execute(productId);

    if (!productsListed) {
      return res.status(400).json({
        message: 'Problemas para encontrar produto.',
      });
    }

    return res.status(200).json({
      message: 'Produtos listados com sucesso!',
      data: productsListed,
    });
  }
);

export default productsRouter;
