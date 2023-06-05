import { Router, Request, Response } from 'express';
import ListProducts from './services/list-products';

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

    return res.json({
      message: 'Produtos listados com sucesso!',
      data: productsListed,
    });
  }
);

export default productsRouter;
