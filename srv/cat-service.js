const cds = require('@sap/cds')

module.exports = class CatalogService extends cds.ApplicationService { init() {
  const { Books } = this.entities

  // discount label on well-stocked books
  this.after('each', Books, book => {
    if (book.stock > 100) book.title += ' -- 11% off!'
  })

  // implement the custom action
  this.on('submitOrder', async req => {
    const { book, quantity } = req.data
    const n = await UPDATE(Books, book)
      .with`stock = stock - ${quantity}`
      .where`stock >= ${quantity}`
    if (!n) return req.error(409, `${quantity} exceeds stock for book #${book}`)
  })

  return super.init()
}}
