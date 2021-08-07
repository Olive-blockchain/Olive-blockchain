const Big = require('big.js');
const units = require('./units');

// TODO: use bigint instead of float
const convert = (amount, from, to) => {
  if (Number.isNaN(Number.parseFloat(amount)) || !Number.isFinite(amount)) {
    return 0;
  }

  const amountInFromUnit = Big(amount).times(units.getUnit(from));

  return Number.parseFloat(amountInFromUnit.div(units.getUnit(to)));
};

class olive {
  constructor(value, unit) {
    this._value = value;
    this._unit = unit;
  }

  to(newUnit) {
    this._value = convert(this._value, this._unit, newUnit);
    this._unit = newUnit;

    return this;
  }

  value() {
    return this._value;
  }

  format() {
    const displayUnit = units.getDisplay(this._unit);

    const { format, fractionDigits, trailing } = displayUnit;

    let options = { maximumFractionDigits: fractionDigits };

    if (trailing) {
      options = { minimumFractionDigits: fractionDigits };
    }

    let value;

    if (fractionDigits !== undefined) {
      const fractionPower = Big(10).pow(fractionDigits);
      value = Number.parseFloat(
        Big(Math.floor(Big(this._value).times(fractionPower))).div(
          fractionPower,
        ),
      );
    } else {
      value = this._value;
    }

    let formatted = format.replace(
      '{amount}',
      Number.parseFloat(value).toLocaleString(undefined, options),
    );

    if (displayUnit.pluralize && this._value !== 1) {
      formatted += 's';
    }

    return formatted;
  }

  toString() {
    const displayUnit = units.getDisplay(this._unit);
    const { fractionDigits } = displayUnit;
    const options = { maximumFractionDigits: fractionDigits };
    return Number.parseFloat(this._value).toLocaleString(undefined, options);
  }
}

export const olive_formatter = (value, unit) => new olive(value, unit);

olive_formatter.convert = convert;
olive_formatter.setDisplay = units.setDisplay;
olive_formatter.setUnit = units.setUnit;
olive_formatter.getUnit = units.getUnit;
olive_formatter.setFiat = (currency, rate, display = null) => {
  units.setUnit(currency, 1 / rate, display);
};

export const dog_to_olive = (dog) => {
  return olive_formatter(Number.parseInt(dog), 'dog').to('olive').value();
};

export const olive_to_dog = (olive) => {
  return olive_formatter(Number.parseFloat(Number(olive)), 'olive')
    .to('dog')
    .value();
};

export const dog_to_olive_string = (dog) => {
  return olive_formatter(Number(dog), 'dog').to('olive').toString();
};

export const dog_to_colouredcoin = (dog) => {
  return olive_formatter(Number.parseInt(dog), 'dog')
    .to('colouredcoin')
    .value();
};

export const colouredcoin_to_dog = (colouredcoin) => {
  return olive_formatter(Number.parseFloat(Number(colouredcoin)), 'colouredcoin')
    .to('dog')
    .value();
};

export const dog_to_colouredcoin_string = (dog) => {
  return olive_formatter(Number(dog), 'dog').to('colouredcoin').toString();
};
