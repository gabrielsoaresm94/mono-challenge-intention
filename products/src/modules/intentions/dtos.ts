interface IRating {
  rate: Number;
  count: Number;
}

export interface IProduct {
  id: Number;
  title: String;
  price: Number;
  category: String;
  description: String;
  image: String;
  rating: IRating
}

export enum IntentionStatus {
  EM_SELECAO = 'EM_SELECAO',
  SELECIONADO = 'SELECIONADO',
}

export interface IIntentionProduct {
  product_id: Number;
  title: String;
  price: Number;
  category: String;
  description: String;
  image: String;
  quantity: Number | null;
  intention_id: Number;
}
