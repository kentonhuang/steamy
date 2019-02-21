import React, { Component } from 'react'

import classes from './SearchBox.module.css'
import SearchBar from '../SearchBar/SearchBar';

export default class SearchBox extends Component {
  render() {
    return (
      <div className={classes.SearchBox}>
        <SearchBar {...this.props}/>
      </div>
    )
  }
}