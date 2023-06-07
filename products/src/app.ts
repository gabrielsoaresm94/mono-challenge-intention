import express, { Router, Request, Response } from 'express';
import swaggerJSDoc from 'swagger-jsdoc';
import swaggerUi from 'swagger-ui-express';
import bodyParser from 'body-parser';

import routes from './routes';

const app = express();
const port = 3001;

app.get('/', (req: Request, res: Response) => {
  res.json({
    success: true
  });
});

const swaggerDefinition = {
  info: {
    title: 'Products Service API',
    version: '1.0.0',
    description: 'A service of products',
  },
  basePath: '/v1',
};

const options = {
  swaggerDefinition,
  apis: ['*/**/controllers.ts'],
};

app.use(bodyParser.json())
app.use(express.json());
app.use('/v1', routes);

const swaggerSpec = swaggerJSDoc(options);
app.use('/v1/docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
