import Unit from './Unit';
import { IS_MAINNET } from './constants';

export default {
  [Unit.OLIVE]: IS_MAINNET ? 'XKA' : 'TXKA',
};
