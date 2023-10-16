interface CRUD_Repository<T> {
  create: (entity: T) => T
  read: (id: string | number) => T | T[] | null
  update: (id: string | number) => T | null
  delete: (id: string | number) => T | null
}

class Exemple implements CRUD_Repository<any>{

  create: (entity: any) => any

  read: (id: string | number) => any

  update: (id: string | number) => any

  delete: (id: string | number) => any

}
