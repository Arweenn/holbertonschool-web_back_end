const assert = require('assert')
const calculateNumber = require('./0-calcul.js')

describe('Rounded addition', function() {
  it('should add two non rounded numbers corectly', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.6), 6);
  })

  it('shoud work on negative numbers', function () {
    assert.strictEqual(calculateNumber(1, -3), -2);
    assert.strictEqual(calculateNumber(-1, 3.7), 3);
    assert.strictEqual(calculateNumber(-1.2, -3.7), -5);
  })

  it('should work with 0', function () {
    assert.strictEqual(calculateNumber(1.5, 0), 2)
    assert.strictEqual(calculateNumber(0, 4.5), 5)
    assert.strictEqual(calculateNumber(0, 0), 0)
  })
})
