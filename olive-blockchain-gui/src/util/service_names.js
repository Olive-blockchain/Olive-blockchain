export const service_wallet = 'olive_wallet';
export const service_full_node = 'olive_full_node';
export const service_farmer = 'olive_farmer';
export const service_harvester = 'olive_harvester';
export const service_simulator = 'olive_full_node_simulator';
export const service_daemon = 'daemon';
export const service_plotter = 'olive plots create';

// Corresponds with outbound_message.py NodeTypes
export const service_connection_types = {
  1: 'Full Node',
  2: 'Harvester',
  3: 'Farmer',
  4: 'Timelord',
  5: 'Introducer',
  6: 'Wallet',
  7: 'Plotter',
};
