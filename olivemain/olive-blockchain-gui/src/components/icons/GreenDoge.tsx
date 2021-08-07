import React from 'react';
import { SvgIcon, SvgIconProps } from '@material-ui/core';
import { ReactComponent as oliveIcon } from './images/olive.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={oliveIcon} viewBox="0 0 150 58" {...props} />;
}
