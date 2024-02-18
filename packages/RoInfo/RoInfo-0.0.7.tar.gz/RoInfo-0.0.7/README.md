
# RoInfo

A Roblox API Wrapper for roblox.com which provides multiple features from the roblox website to be used from python.


## Authors

- [@Ryan-shamu-YT](https://github.com/Ryan-shamu-YT/)


## Features

- Groups
- Friends/Followers
- Robux
- Display Names


## API Reference

#### Login

```python
  From RoInfo import Session
  session = Session("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_RestOfTheToken")
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Session` | `string` | **Required**. Your Roblox Account Token |

Upon calling this function you will now be able to use the functions which require an account, e.g. session.sendmessage("RecipentID", "Subject", "Body") sends a message to the Recipent which will require an active session

#### Session Functions

```python
  session.change_display_name("newdisplayname")
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Display Name`      | `string` | **Required**. Display Name To Be Set |



```python
  session.get_current_robux()
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `None`      | `None` | **Returns the amount of roblox under the logged in user's account**.  |


### Groups


```python
  From RoInfo import Groups
```

Most functions under Groups do not require an account, functions which require permission e.g. sendgroupfunds("groupid", "userrecievingfunds", "amount")



| Parameter(s) | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Group Id`, `userid`, `amount`  | `number` | **Required**. Active Session and permission to the action |

Upon calling this function the specified player (`userid`) will receive the specified robux  (`amount`) from the specified group (`groupid`)

**More Documentation Soon!**
