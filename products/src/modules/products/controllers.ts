import { Router, Request, Response } from 'express';

const productsRouter = Router();

/**
 * @swagger
 * /products:
 *   get:
 *     summary: Retorna a lista de produtos.
 *     responses:
 *       200:
 *         description: Lista de produtos retornada com sucesso.
 */
productsRouter.get(
  '/',
  (req: Request, res: Response): Response => {
    return res.json({
      message: 'Produtos listados com sucesso!'
    });
  }
);

export default productsRouter;
