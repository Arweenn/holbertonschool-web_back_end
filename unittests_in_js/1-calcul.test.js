const assert = require('assert')
const calculateNumber = require('./1-calcul')

describe('Addition', function () {
  it('should add two non rounded numbers corectly', function () {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM', 1.5, 3.6), 6);
  })

  it('shoud work on negative numbers', function () {
    assert.strictEqual(calculateNumber('SUM', 1, -3), -2);
    assert.strictEqual(calculateNumber('SUM', -1, 3.7), 3);
    assert.strictEqual(calculateNumber('SUM', -1.2, -3.7), -5);
  })

  it('should work with 0', function () {
    assert.strictEqual(calculateNumber('SUM', 1.5, 0), 2)
    assert.strictEqual(calculateNumber('SUM', 0, 4.5), 5)
    assert.strictEqual(calculateNumber('SUM', 0, 0), 0)
  })
})
describe('Substraction', function () {
  it('should substract two non rounded numbers corectly', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), -2);
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3.7), -3);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.6), -2);
  })

  it('shoud work on negative numbers', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, -3), 4);
    assert.strictEqual(calculateNumber('SUBTRACT', -1, 3.7), -5);
    assert.strictEqual(calculateNumber('SUBTRACT', -1.2, -3.7), 3);
  })

  it('should work with 0', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 0), 2)
    assert.strictEqual(calculateNumber('SUBTRACT', 0, 4.5), -5)
    assert.strictEqual(calculateNumber('SUBTRACT', 0, 0), 0)
  })
})
describe('Division', function () {
  it('should divide two non rounded numbers corectly', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1, 3), 0.3333333333333333);
    assert.strictEqual(calculateNumber('DIVIDE', 1, 3.7), 0.25);
    assert.strictEqual(calculateNumber('DIVIDE', 1.2, 3.7), 0.25);
    assert.strictEqual(calculateNumber('DIVIDE', 1.5, 3.6), 0.5);
  })

  it('shoud work on negative numbers', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1, -3), -0.3333333333333333);
    assert.strictEqual(calculateNumber('DIVIDE', -1, 3.7), -0.25);
    assert.strictEqual(calculateNumber('DIVIDE', -1.2, -3.7), 0.25);
  })

  it('should work with 0', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 1.5, 0), 'Error')
    assert.strictEqual(calculateNumber('DIVIDE', 0, 4.5), 0)
    assert.strictEqual(calculateNumber('DIVIDE', 0, 0), 'Error')
  })
})
describe('Types', function () {
  it('should return Error if type is not string', function () {
    assert.strictEqual(calculateNumber(5, 1, 3), 'Error');
    assert.strictEqual(calculateNumber(['Divide'], 1, 3.7), 'Error');
  })

  it('shoud return undefined if not predefined operation used', function () {
    assert.strictEqual(calculateNumber('MULTIPLY', 1, 3), undefined)
  })
})
