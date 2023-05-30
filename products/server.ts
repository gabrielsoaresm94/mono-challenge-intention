import express, { Request, Response } from 'express';

const app = express();
const port = 3001;

app.get('/v1/hello', (req: Request, res: Response) => {
  res.json({
    message: 'Hello, world!'
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
