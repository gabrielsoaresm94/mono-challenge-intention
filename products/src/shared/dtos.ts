export interface IResponse<T> {
  message: String;
  status: boolean;
  data: T;
}
