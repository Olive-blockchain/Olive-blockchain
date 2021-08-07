const olive = require('../../util/olive');

describe('olive', () => {
  it('converts number dog to olive', () => {
    const result = oliveblockchain.co_to_olive(1000000);

    expect(result).toBe(0.000001);
  });
  it('converts string dog to olive', () => {
    const result = oliveblockchain.co_to_olive('1000000');

    expect(result).toBe(0.000001);
  });
  it('converts number dog to olive string', () => {
    const result = oliveblockchain.co_to_olive_string(1000000);

    expect(result).toBe('0.000001');
  });
  it('converts string dog to olive string', () => {
    const result = oliveblockchain.co_to_olive_string('1000000');

    expect(result).toBe('0.000001');
  });
  it('converts number olive to dog', () => {
    const result = olive.olive_to_dog(0.000001);

    expect(result).toBe(1000000);
  });
  it('converts string olive to dog', () => {
    const result = olive.olive_to_dog('0.000001');

    expect(result).toBe(1000000);
  });
  it('converts number dog to colouredcoin', () => {
    const result = oliveblockchain.co_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it('converts string dog to colouredcoin', () => {
    const result = oliveblockchain.co_to_colouredcoin('1000000');

    expect(result).toBe(1000);
  });
  it('converts number dog to colouredcoin string', () => {
    const result = oliveblockchain.co_to_colouredcoin_string(1000000);

    expect(result).toBe('1,000');
  });
  it('converts string dog to colouredcoin string', () => {
    const result = oliveblockchain.co_to_colouredcoin_string('1000000');

    expect(result).toBe('1,000');
  });
  it('converts number colouredcoin to dog', () => {
    const result = olive.colouredcoin_to_dog(1000);

    expect(result).toBe(1000000);
  });
  it('converts string colouredcoin to dog', () => {
    const result = olive.colouredcoin_to_dog('1000');

    expect(result).toBe(1000000);
  });
});
