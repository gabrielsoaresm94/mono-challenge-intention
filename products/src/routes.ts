import express, { Router } from 'express';
import productsRouter from './modules/products/controllers';

const routes = Router();

routes.use('/products', productsRouter);

export default routes;