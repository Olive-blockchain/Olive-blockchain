import React, { useState } from "react"
import { t } from '@lingui/macro';
import { Box, IconButton, Paper } from '@material-ui/core';
import { Search as SearchIcon } from '@material-ui/icons';
import { useHistory } from 'react-router-dom';
import styled from 'styled-components';
import { Flex, Form, InputBase } from '@olive/core';
import { useForm } from 'react-hook-form';

import {
  Typography,
  Button,
} from '@material-ui/core';

import {
  get_coin_records_by_puzzle_hash,
  push_tx,
} from '../../modules/fullnodeMessages';

import {
  recover_pool_nft
} from '../../modules/message';

import { useDispatch } from 'react-redux';
import { date } from '@lingui/core/cjs/formats';

import { address_to_puzzle_hash } from './address_to_puzzle_hash' 

const StyledInputBase = styled(InputBase)`
  min-width: 15rem;
`;

type FormData = {
  poolAddress: string;
  qdId: string;
};

var can_records = new Array()
var pool_contract_hash = ""

export default function PoolCollection() {

  function dealSearchResult(records:any[]):string {

    var total: number = 0
    var can: number = 0
    var temp = new Array()

    var record: any
    for(let record of records) {
      var amount: number = record.coin.amount
      var timestamp: number = record.timestamp

      total += amount
      var current = (new Date()).getTime()/1000
      if ((current-timestamp)>604800) {
        can += amount
        temp.push(record.coin)
      }
    }

    can_records = temp
    return "Total Coins Not Recovered:" + total/1000000000000 + "<br/>" + "Total Coins Can Recovered:" + can/1000000000000
  }


  //==================================
  const dispatch = useDispatch();

  const methods = useForm<FormData>({
    shouldUnregister: false,
    defaultValues: {
      poolAddress: '',
      qdId: '',
    },
  });

  async function handleSearch(values: FormData) {
    let address = values.poolAddress
    if (address) {
      pool_contract_hash = ""
      can_records = new Array()
      setContent(" ")

      try {
        let puzzlehash = address_to_puzzle_hash(address)
        const data = await dispatch(get_coin_records_by_puzzle_hash(puzzlehash));
        if (data.success) {
          pool_contract_hash = puzzlehash
          let result = dealSearchResult(data.coin_records)
          setContent(result)
        } else {
          alert(data.error)
        }
      } catch (error) {
        alert(error)
      }
    }
  }
  
  async function handleCollection(values: FormData) {
    let qdId = values.qdId
    if (!qdId) {
      alert("Input NFT Launcher Id")
      return
    }
    if (can_records.length < 1) {
      alert("Can not find any coins to recover, please enter the correct pool contract address and search.")
      return
    }

    try {
      console.log("======")
      console.log(can_records)
      const data = await dispatch(recover_pool_nft(pool_contract_hash, qdId, can_records));
      console.log(data)
      console.log("======")
      if (data.success) {
        let spend_bundle = data.spend_bundle
        console.log(spend_bundle)
        const pushTxData = await dispatch(push_tx(spend_bundle));
        console.log(pushTxData)
        if (pushTxData.success) {
          alert("success")
        } else {
          alert(pushTxData.error)
        }
      } else {
        alert(data.error)
      }
    } catch (error) {
      alert(error)
    }
  }


  const [typography, setContent] = useState(" ")
  return (
    <Flex flexDirection="column" gap={3}>

      <Typography variant="body1" color="textSecondary">
        Enter your chia pool contract address and NFT Launcher ID to recover the missing XOL from your plot NFT.
      </Typography>

      <Form methods={methods} onSubmit={handleSearch}>
        <Paper elevation={0} variant="outlined">
          <Flex alignItems="center" gap={1}>
            <Box />
            <StyledInputBase
              name="poolAddress"
              placeholder='Pool Contract Address'
              fullWidth
            />
            <IconButton type="submit" aria-label="search">
              <SearchIcon />
            </IconButton>
          </Flex>
        </Paper>
      </Form>

      <Typography variant="body1" color="textSecondary"  dangerouslySetInnerHTML={{__html: typography}}>
      </Typography>

      <Form methods={methods} onSubmit={handleCollection}>
      <Paper elevation={0} variant="outlined">
          <Flex alignItems="center" gap={1}>
            <Box />
            <StyledInputBase
              name="qdId"
              placeholder='NFT Launcher Id'
              fullWidth
            />
            <Button variant="contained" color="primary" type="submit">
              RECOVER
            </Button>
          </Flex>
        </Paper>
      </Form>

    </Flex>
  );
}
