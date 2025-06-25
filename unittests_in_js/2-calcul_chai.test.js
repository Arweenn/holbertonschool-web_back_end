const { expect } = require('chai')
const calculateNumber = require('./2-calcul_chai')

describe('Addition', function () {
  it('should add two non rounded numbers corectly', function () {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
    expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
    expect(calculateNumber('SUM', 1.5, 3.6)).to.equal(6);
  })

  it('shoud work on negative numbers', function () {
    expect(calculateNumber('SUM', 1, -3)).to.equal(-2);
    expect(calculateNumber('SUM', -1, 3.7)).to.equal(3);
    expect(calculateNumber('SUM', -1.2, -3.7)).to.equal(-5);
  })

  it('should work with 0', function () {
    expect(calculateNumber('SUM', 1.5, 0)).to.equal(2)
    expect(calculateNumber('SUM', 0, 4.5)).to.equal(5)
    expect(calculateNumber('SUM', 0, 0)).to.equal(0)
  })
})
describe('Substraction', function () {
  it('should substract two non rounded numbers corectly', function () {
    expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
    expect(calculateNumber('SUBTRACT', 1, 3.7)).to.equal(-3);
    expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.equal(-3);
    expect(calculateNumber('SUBTRACT', 1.5, 3.6)).to.equal(-2);
  })

  it('shoud work on negative numbers', function () {
    expect(calculateNumber('SUBTRACT', 1, -3)).to.equal(4);
    expect(calculateNumber('SUBTRACT', -1, 3.7)).to.equal(-5);
    expect(calculateNumber('SUBTRACT', -1.2, -3.7)).to.equal(3);
  })

  it('should work with 0', function () {
    expect(calculateNumber('SUBTRACT', 1.5, 0)).to.equal(2)
    expect(calculateNumber('SUBTRACT', 0, 4.5)).to.equal(-5)
    expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0)
  })
})
describe('Division', function () {
  it('should divide two non rounded numbers corectly', function () {
    expect(calculateNumber('DIVIDE', 1, 3)).to.equal(0.3333333333333333);
    expect(calculateNumber('DIVIDE', 1, 3.7)).to.equal(0.25);
    expect(calculateNumber('DIVIDE', 1.2, 3.7)).to.equal(0.25);
    expect(calculateNumber('DIVIDE', 1.5, 3.6)).to.equal(0.5);
  })

  it('shoud work on negative numbers', function () {
    expect(calculateNumber('DIVIDE', 1, -3)).to.equal(-0.3333333333333333);
    expect(calculateNumber('DIVIDE', -1, 3.7)).to.equal(-0.25);
    expect(calculateNumber('DIVIDE', -1.2, -3.7)).to.equal(0.25);
  })

  it('should work with 0', function () {
    expect(calculateNumber('DIVIDE', 1.5, 0)).to.equal('Error')
    expect(calculateNumber('DIVIDE', 0, 4.5)).to.equal(0)
    expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error')
  })
})
describe('Types', function () {
  it('should return Error if type is not string', function () {
    expect(calculateNumber(5, 1, 3)).to.equal('Error');
    expect(calculateNumber(['Divide'], 1, 3.7)).to.equal('Error');
  })

  it('shoud return undefined if not predefined operation used', function () {
    expect(calculateNumber('MULTIPLY', 1, 3)).to.equal(undefined)
  })
})
