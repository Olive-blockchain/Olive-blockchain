import React from 'react';
import { SvgIcon, SvgIconProps } from '@material-ui/core';
import { ReactComponent as OliveIcon } from './images/olive.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={OliveIcon} viewBox="0 0 150 58" {...props} />;
}
