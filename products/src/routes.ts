import { Router } from 'express';
import productsRouter from './modules/products/controllers';
import intentionsRouter from './modules/intentions/controllers';

const routes = Router();

routes.use('/intentions', intentionsRouter);
routes.use('/products', productsRouter);

export default routes;