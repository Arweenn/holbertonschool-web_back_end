const chai = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment.js');

describe('sendPaymentRequestToApi', function () {
  let consoleLogSpy;

  beforeEach(function () {
    consoleLogSpy = sinon.spy(console, 'log');
  })

  afterEach(function () {
    consoleLogSpy.restore();
  })

  it('sendPayementRequestToAPI with 100 & 20', () => {
    sendPaymentRequestToApi(100, 20);
    chai.expect(consoleLogSpy.calledOnce).to.be.true;
    chai.expect(consoleLogSpy.calledWith('The total is: 120')).to.be.true;
  });

  it('sendPayementRequestToAPI with 10 & 10', function () {
    sendPaymentRequestToApi(10, 10);
    chai.expect(consoleLogSpy.calledOnce).to.be.true;
    chai.expect(consoleLogSpy.calledWith('The total is: 20')).to.be.true;
  })
});
