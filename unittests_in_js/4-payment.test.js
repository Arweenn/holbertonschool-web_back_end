const chai = require('chai');
const sinon = require('sinon');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./3-payment.js');

describe('sendPaymentRequestToApi', function () {
  const calculateNumberStub = sinon.stub(Utils, 'calculateNumber');
  calculateNumberStub.returns(10);
  const consoleLogSpy = sinon.spy(console, 'log');

  it('validate the usage of the Utils function', () => {
    sendPaymentRequestToApi(100, 20);

    chai.expect(calculateNumberStub.calledOnce).to.be.true;
    chai.expect(calculateNumberStub.calledWith('SUM', 100, 20)).to.be.true;
    chai.expect(consoleLogSpy.calledWith('The total is: 10')).to.be.true;

    calculateNumberStub.restore();
    consoleLogSpy.restore();
  });
});
