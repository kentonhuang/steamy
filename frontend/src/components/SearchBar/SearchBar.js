import React, { Component } from 'react'

import classes from './SearchBar.module.css'

export default class SearchBar extends Component {
  render() {
    return (
        <form className={classes.Form} onSubmit={this.props.submit}>
            <label className={classes.Bar}>
                <input type="text" name="steamid" value={this.props.value} onChange={this.props.change}/>
            </label>
            <input className={classes.Button} type="submit" value="SEARCH" />
        </form>
    )
  }
}
