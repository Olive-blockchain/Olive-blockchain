const olive = require('../../util/olive');

describe('olive', () => {
  it('converts number mojo to olive', () => {
    const result = olive.mojo_to_olive(1000000);

    expect(result).toBe(0.000001);
  });
  it('converts string mojo to olive', () => {
    const result = olive.mojo_to_olive('1000000');

    expect(result).toBe(0.000001);
  });
  it('converts number mojo to olive string', () => {
    const result = olive.mojo_to_olive_string(1000000);

    expect(result).toBe('0.000001');
  });
  it('converts string mojo to olive string', () => {
    const result = olive.mojo_to_olive_string('1000000');

    expect(result).toBe('0.000001');
  });
  it('converts number olive to mojo', () => {
    const result = olive.olive_to_mojo(0.000001);

    expect(result).toBe(1000000);
  });
  it('converts string olive to mojo', () => {
    const result = olive.olive_to_mojo('0.000001');

    expect(result).toBe(1000000);
  });
  it('converts number mojo to colouredcoin', () => {
    const result = olive.mojo_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it('converts string mojo to colouredcoin', () => {
    const result = olive.mojo_to_colouredcoin('1000000');

    expect(result).toBe(1000);
  });
  it('converts number mojo to colouredcoin string', () => {
    const result = olive.mojo_to_colouredcoin_string(1000000);

    expect(result).toBe('1,000');
  });
  it('converts string mojo to colouredcoin string', () => {
    const result = olive.mojo_to_colouredcoin_string('1000000');

    expect(result).toBe('1,000');
  });
  it('converts number colouredcoin to mojo', () => {
    const result = olive.colouredcoin_to_mojo(1000);

    expect(result).toBe(1000000);
  });
  it('converts string colouredcoin to mojo', () => {
    const result = olive.colouredcoin_to_mojo('1000');

    expect(result).toBe(1000000);
  });
});
