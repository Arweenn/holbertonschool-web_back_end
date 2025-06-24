const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function() {
  it('should return 4', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });
  it('should return 5', () => {
    assert.strictEqual(calculateNumber(1.9, 3), 5);
  });
  it('should return 5', () => {
    assert.strictEqual(calculateNumber(1.4, 3.5), 5);
  });
  it('should return 6', () => {
    assert.strictEqual(calculateNumber(1.4, 3.5), 5);
  });

  it('negative numbers', () => {
    assert.strictEqual(calculateNumber(-1, 1), 0);
    assert.strictEqual(calculateNumber(1, -1), 0);
    assert.strictEqual(calculateNumber(-1, -1), -2);
  });

  it('checks arguments', () => {
    assert.strictEqual(isNaN(calculateNumber(1)), true);
    assert.strictEqual(isNaN(calculateNumber()), true);
  });
});
