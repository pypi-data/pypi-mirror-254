# import libraries
import mutagen
import tinytag
import os
from json import loads
from PIL import Image
from base64 import b64decode
from re import findall
from random import randint, choice
import datetime
import asyncio, aiohttp
from arsein.Clien import clien
from arsein.TypeText import TypeText, makeJsonResend
from arsein.Device import DeviceTelephone
from arsein.PostData import method_Rubika
from arsein.Getheader import Upload
from arsein.Encoder import encoderjson, getThumbInline
from arsein.Error import AuthError, TypeMethodError, ErrorMethod, ErrorPrivatyKey
from arsein.Copyright import copyright
from mutagen.mp3 import MP3
from tinytag import TinyTag
import base64
import io
import httpx


class Messenger:
    def __init__(self, Sh_account: str, keyAccount: str, TypePlat: str = None):
        keyAccount = keyAccount.replace(
            "-----BEGIN RSA PRIVATE KEY-----\n", ""
        ).replace("\n-----END RSA PRIVATE KEY-----", "")
        self.keyUser, status_platform = (
            keyAccount if keyAccount.endswith("==") else keyAccount + "==",
            "",
        )

        # check Auth Account
        if Sh_account.__len__() != 32:
            raise AuthError("The Auth entered is incorrect")

        # check PrivatyKey Account
        if self.keyUser[:3] == "eyJ":
            status_platform = "web"
            self.cli = clien("web").platform
            self.keyUser = loads(b64decode(self.keyUser).decode("utf-8"))["d"]

        elif self.keyUser[:3] == "MII":
            status_platform = "android"
            self.cli = clien("android").platform
            self.keyUser = f"-----BEGIN RSA PRIVATE KEY-----\n{self.keyUser}\n-----END RSA PRIVATE KEY-----"
        elif not "android" or "web" in status_platform:
            raise ErrorPrivatyKey("Your account private key is incorrect")

        # get Data
        self.CopyRight = copyright.CopyRight
        self.Auth = encoderjson.changeAuthType("".join(findall(r"\w", Sh_account)))
        self.OrginalAuth = "".join(findall(r"\w", Sh_account))
        self.TypePlatform = status_platform
        self.methods = method_Rubika(
            plat=status_platform,
            OrginalAuth=Sh_account,
            auth=self.Auth,
            keyAccount=self.keyUser,
        )
        self.Upload = Upload(status_platform, self.OrginalAuth, self.Auth, self.keyUser)

    def __repr__(self):
        return f"Auth your Account: {self.Auth} and PrivateKey: {self.keyUser.replace('-----BEGIN RSA PRIVATE KEY-----','').replace('-----END RSA PRIVATE KEY-----','')[:50]} ...."

    @property
    def thumb_inline(self):
        return "/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABtbnRyUkdCIFhZWiAH4AABAAEAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAACRyWFlaAAABFAAAABRnWFlaAAABKAAAABRiWFlaAAABPAAAABR3dHB0AAABUAAAABRyVFJDAAABZAAAAChnVFJDAAABZAAAAChiVFJDAAABZAAAAChjcHJ0AAABjAAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJYWVogAAAAAAAAb6IAADj1AAADkFhZWiAAAAAAAABimQAAt4UAABjaWFlaIAAAAAAAACSgAAAPhAAAts9YWVogAAAAAAAA9tYAAQAAAADTLXBhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACAAAAAcAEcAbwBvAGcAbABlACAASQBuAGMALgAgADIAMAAxADb/2wBDAAMCAgICAgMCAgIDAwMDBAYEBAQEBAgGBgUGCQgKCgkICQkKDA8MCgsOCwkJDRENDg8QEBEQCgwSExIQEw8QEBD/2wBDAQMDAwQDBAgEBAgQCwkLEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBD/wAARCAAoACgDASIAAhEBAxEB/8QAGwAAAgMAAwAAAAAAAAAAAAAAAAYFBwgDBAn/xAAwEAACAQIGAQMCAwkAAAAAAAABAgMEEQAFBhIhMUEHE3EUIlFhkQgVFiMyM0Jigf/EABkBAAMBAQEAAAAAAAAAAAAAAAMEBgUHAv/EACgRAAEDBAECBQUAAAAAAAAAAAECAwQABREhMRITBhQiQVFhcYHR4f/aAAwDAQACEQMRAD8AwbTZfWVtTAqQ+/UysIY5IjuknZjZVN+x46ueicSNVpSfL82lyiqoHpamnmaGancfzIZASpRierHi3jDDlGXVMczstVHKJEMW6MhlZQw7BF+bcLx+PfBe8n0IlfmzQmmnhBb74pUZXQ+Q265/Un/mOwRbUme2XFjOd5P7rmEq9mMvpBqo0yB1QqYTu2t45HBHzjqzZHtJkWIC4II8gkfrjZlN6SJNlsJFHAWipmpw306glWJJJNuWuT9x56wg6m9GK/J44s6r9OZt+6JX9v6iKmdEkJuAqSFdhNx1zexx7assNPo9/b70NV8kq9SuKy1U5a0IcbCQwt0eOcGH6v0e8NTJT1jLTzBtghljbeWvb+m3jyfGDGNKsyQ6QAK1o92y2CVU4adpkqpqeigp6yovKiq6Q+y+7cPF/uubfHHk41v6XZBoLMKHW2Z6vqa6rziXN6GnoKmtljkzP25A5dgjSBGJcRh5LttUkg3xh7LtTVEdSk1PGI3G11kV2uF/xC36HfycXB6e+r2b5RUy7MxZTUywyzlrMXeJt8bXPN1bkfnilYQ4/C7KF4OsEa0CDz9QPzUrIR5eX3lpyMHIO+RjjjVeiesH9LtNZZJU6Y0jpfMDDKYAgryysnQIjV7k7gwLmwAseb4rH9oXVGmMs0FDkeTakptv8SU5TL8srWkjSlSkR5AkPuOoVagtY+XuRioq71f1HLQzU/1btup5nlU2O6Ocgy3/ACcgE/GKY1x6qZxnMS0NZmkslPFUvVogbhJnsHkH+x2rc/kMKQPDrjDrbz689Jzsk5+Of5zRZd6TLbWyyjHUMaAGPnjdLnqbmVLX6uzWqpq7MJIWqOUkAp5VIFjzawta1rDxcYMJeo85q2naumLVX1ckh92oJcSk9sSSCzG/XBvyfABgVzda8waPAjL7Aqu6HOmiXaztZQdv3Ec/OJKj1C8NikpBwYMT0Oe+GE4NVcuGyp45FT7a0rhFvNfNveIKT7h66t8cY4J9XUs+VvTVFKDVtMrLWGVrpEAQU9vprmx3Hni3nBgw09eJYWE9WsChN2qKnYTS9V1T1E7KjRyOwvGZD/cXwF/E98ceR3xgwYMLoSZJK1k5zTwbQhICUiv/2Q=="

    # MentionText Mono Bold Italic Strike Underline Spoiler hyperlink
    def sendMessage(
        self, guid, text, Type=None, link=None, Guid_mention=None, message_id=None
    ):
        if Type != None:
            if Type == "MentionText":
                if Guid_mention != None:
                    return self.methods.methodsRubika(
                        "json",
                        methode="sendMessage",
                        indata={
                            "object_guid": guid,
                            "rnd": f"{randint(100000,999999)}",
                            "text": text,
                            "metadata": {
                                "meta_data_parts": TypeText(
                                    "MentionText", text, guid=Guid_mention
                                )
                            },
                            "reply_to_message_id": message_id,
                        },
                        wn=self.cli,
                    )
            elif Type != "MentionText" and Type != "Bot" and Type != "hyperlink":
                return self.methods.methodsRubika(
                    "json",
                    methode="sendMessage",
                    indata={
                        "object_guid": guid,
                        "rnd": f"{randint(100000,999999)}",
                        "text": text,
                        "metadata": {"meta_data_parts": TypeText(Type, text=text)},
                        "reply_to_message_id": message_id,
                    },
                    wn=self.cli,
                )
            elif Type == "hyperlink":
                return self.methods.methodsRubika(
                    "json",
                    methode="sendMessage",
                    indata={
                        "object_guid": guid,
                        "rnd": f"{randint(100000,999999)}",
                        "text": text,
                        "metadata": {
                            "meta_data_parts": TypeText(Type, text=text, link=link)
                        },
                        "reply_to_message_id": message_id,
                    },
                    wn=self.cli,
                )
            elif Type == "Bot":
                if text == "سؤال دارم":
                    return self.methods.methodsRubika(
                        "json",
                        methode="sendMessage",
                        indata={
                            "object_guid": guid,
                            "rnd": f"{randint(100000,999999)}",
                            "text": text,
                            "aux_data": {"button_id": "question"},
                        },
                        wn=self.cli,
                    )
                elif text == "سؤالات من":
                    return self.methods.methodsRubika(
                        "json",
                        methode="sendMessage",
                        indata={
                            "object_guid": guid,
                            "rnd": f"{randint(100000,999999)}",
                            "text": text,
                            "aux_data": {"button_id": "my_questions"},
                        },
                        wn=self.cli,
                    )
                elif text == "گزارش محتوای خلاف قوانین":
                    return self.methods.methodsRubika(
                        "json",
                        methode="sendMessageAPICall",
                        indata={
                            "text": text,
                            "object_guid": guid,
                            "message_id": message_id,
                            "aux_data": {"button_id": "faq_5f0069d7108cd24b2a958dad"},
                        },
                        wn=self.cli,
                    )
                elif text == "سؤال از پشتیبانی":
                    return self.methods.methodsRubika(
                        "json",
                        methode="sendMessageAPICall",
                        indata={
                            "text": text,
                            "object_guid": guid,
                            "message_id": message_id,
                            "aux_data": {
                                "button_id": "newtextq_5e946df25ed39a95b3c225d9"
                            },
                        },
                        wn=self.cli,
                    )
        elif Type == None:
            return self.methods.methodsRubika(
                "json",
                methode="sendMessage",
                indata={
                    "object_guid": guid,
                    "rnd": f"{randint(100000,999999)}",
                    "text": text,
                    "reply_to_message_id": message_id,
                },
                wn=self.cli,
            )

    def editMessage(self, guid, new, message_id):
        return self.methods.methodsRubika(
            "json",
            methode="editMessage",
            indata={"message_id": message_id, "object_guid": guid, "text": new},
            wn=self.cli,
        )

    def deleteMessages(self, guid, message_ids):
        return self.methods.methodsRubika(
            "json",
            methode="deleteMessages",
            indata={"object_guid": guid, "message_ids": message_ids, "type": "Global"},
            wn=self.cli,
        )

    def getMessagefilter(self, guid, filter_whith):
        return (
            self.methods.methodsRubika(
                "json",
                methode="getMessages",
                indata={
                    "filter_type": filter_whith,
                    "max_id": "NaN",
                    "object_guid": guid,
                    "sort": "FromMax",
                },
                wn=self.cli,
            )
            .get("data")
            .get("messages")
        )

    def getMessages(self, guid, min_id):
        return (
            self.methods.methodsRubika(
                "json",
                methode="getMessagesInterval",
                indata={"object_guid": guid, "middle_message_id": min_id},
                wn=self.cli,
            )
            .get("data")
            .get("messages")
        )

    def getMessagesbySort(self, guid, message_id, Type):
        if Type == "max":
            return self.methods.methodsRubika(
                "json",
                methode="getMessagesInterval",
                indata={"object_guid": guid, "sort": "FromMax", "max_id": message_id},
                wn=self.cli,
            )
        elif Type == "min":
            return self.methods.methodsRubika(
                "json",
                methode="getMessagesInterval",
                indata={"object_guid": guid, "sort": "FromMin", "min_id": message_id},
                wn=self.cli,
            )

    def searchMessages(self, guid, text):
        return self.methods.methodsRubika(
            "json",
            methode="searchChatMessages",
            indata={
                "search_text": text.replace("#", ""),
                "type": "Hashtag" if text.startswith("#") else "Text",
                "object_guid": guid,
            },
            wn=self.cli,
        )  # Hashtag #Text.....

    def getChats(self, start_id=None):
        return self.methods.methodsRubika(
            "json", methode="getChats", indata={"start_id": start_id}, wn=self.cli
        )

    def getMapView(self, latitude, longitude):
        return self.methods.methodsRubika(
            "json",
            methode="getMapView",
            indata={"location": {"latitude": latitude, "longitude": longitude}},
            wn=self.cli,
        )

    def sendMap(self, guid, latitude, longitude):
        return self.methods.methodsRubika(
            "json",
            methode="sendMessage",
            indata={
                "object_guid": guid,
                "rnd": randint(100000, 999999999),
                "location": {"latitude": latitude, "longitude": longitude},
            },
            wn=self.cli,
        )

    def getMessagesUpdates(self, guid):
        state = str(round(datetime.datetime.today().timestamp()) - 200)
        return self.methods.methodsRubika(
            "json",
            methode="getMessagesUpdates",
            indata={"object_guid": guid, "state": state},
            wn=self.cli,
        )

    @property
    def getChatsUpdate(self):
        state = str(round(datetime.datetime.today().timestamp()) - 200)
        return self.methods.methodsRubika(
            "json", methode="getChatsUpdates", indata={"state": state}, wn=self.cli
        )

    def deleteUserChat(self, user_guid, last_message):
        return self.methods.methodsRubika(
            "json",
            methode="deleteUserChat",
            indata={"last_deleted_message_id": last_message, "user_guid": user_guid},
            wn=self.cli,
        )

    def startSupperBot(self, guid):
        return self.methods.methodsRubika(
            "json",
            methode="sendMessage",
            indata={
                "object_guid": guid,
                "rnd": randint(100000, 999999),
                "text": "/start",
            },
            wn=self.cli,
        )

    def stoptSupperBot(self, guid):
        return self.methods.methodsRubika(
            "json", methode="stopBot", indata={"bot_guid": guid}, wn=self.cli
        )

    def sendChatActivity(self, user_guid):
        return self.methods.methodsRubika(
            "json",
            methode="sendChatActivity",
            indata={"object_guid": user_guid, "activity": "Typing"},
            wn=self.cli,
        )

    def getInfoByUsername(self, username):
        return self.methods.methodsRubika(
            "json",
            methode="getObjectByUsername",
            indata={"username": username.replace("@", "")},
            wn=self.cli,
        )

    def banGroupMember(self, guid_gap, user_id):
        return self.methods.methodsRubika(
            "json",
            methode="banGroupMember",
            indata={"group_guid": guid_gap, "member_guid": user_id, "action": "Set"},
            wn=self.cli,
        )

    def unbanGroupMember(self, guid_gap, user_id):
        return self.methods.methodsRubika(
            "json",
            methode="banGroupMember",
            indata={"group_guid": guid_gap, "member_guid": user_id, "action": "Unset"},
            wn=self.cli,
        )

    def banChannelMember(self, guid_channel, user_id):
        return self.methods.methodsRubika(
            "json",
            methode="banChannelMember",
            indata={
                "channel_guid": guid_channel,
                "member_guid": user_id,
                "action": "Set",
            },
            wn=self.cli,
        )

    def unbanChannelMember(self, guid_channel, user_id):
        return self.methods.methodsRubika(
            "json",
            methode="banChannelMember",
            indata={
                "channel_guid": guid_channel,
                "member_guid": user_id,
                "action": "Unset",
            },
            wn=self.cli,
        )

    def shaireContect(self, guid, phone_number, first_name, last_name=None):
        return self.methods.methodsRubika(
            "json",
            methode="sendMessage",
            indata={
                "object_guid": "u09pbi05e46fa119166489d14a3f0562",
                "type": "ContactMessage",
                "message_contact": {
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": f"98{phone_number[1:]}",
                    "user_guid": guid,
                },
                "rnd": randint(100000, 999999),
            },
            wn=self.cli,
        )

    # report account or channell or group
    def report(self, guid, reportType):
        if not reportType in [102, 101, 104, 103, 105, 106, 100]:
            raise ErrorMethod("the numerTypeReport is wrong! ")
        else:
            return self.methods.methodsRubika(
                "json",
                methode="reportObject",
                indata={
                    "object_guid": guid,
                    "report_type": reportType,
                    "report_type_object": "Object",
                },
                wn=self.cli,
            )

    def reportPost(self, guid, reportType, message_ids):
        if not reportType in [102, 101, 104, 103, 105, 106, 100]:
            raise ErrorMethod("the numerTypeReport is wrong ! ")
        else:
            return self.methods.methodsRubika(
                "json",
                methode="reportObject",
                indata={
                    "object_guid": guid,
                    "message_id": message_ids,
                    "report_type": reportType,
                    "report_type_object": "Message",
                },
                wn=self.cli,
            )

    def otherReport(self, TYPE, guid, text, message_ids=None):
        if TYPE == "message":
            if message_ids != None:
                return self.methods.methodsRubika(
                    "json",
                    methode="reportObject",
                    indata={
                        "object_guid": guid,
                        "message_id": message_ids,
                        "report_type": 100,
                        "report_type_object": "Message",
                        "report_description": text,
                    },
                    wn=self.cli,
                )
            else:
                raise ErrorMethod("in method report << message_id is None ! >> ")
        elif TYPE == "pv":
            return self.methods.methodsRubika(
                "json",
                methode="reportObject",
                indata={
                    "object_guid": guid,
                    "report_type": 100,
                    "report_type_object": "Object",
                    "report_description": text,
                },
                wn=self.cli,
            )
        elif TYPE == "channel":
            return self.methods.methodsRubika(
                "json",
                methode="reportObject",
                indata={
                    "object_guid": guid,
                    "report_type": 100,
                    "report_type_object": "Object",
                    "report_description": text,
                },
                wn=self.cli,
            )

    def getbanGroupUsers(self, guid_gap, text=None, start_id=None):
        return self.methods.methodsRubika(
            "json",
            methode="getBannedGroupMembers",
            indata={"group_guid": guid_gap, "search_text": text, "start_id": start_id},
            wn=self.cli,
        )

    def getbanChannelUsers(self, guid_channel, text=None, start_id=None):
        return self.methods.methodsRubika(
            "json",
            methode="getBannedChannelMembers",
            indata={
                "channel_guid": guid_channel,
                "search_text": text,
                "start_id": start_id,
            },
            wn=self.cli,
        )

    def getGroupInfo(self, guid_gap):
        return self.methods.methodsRubika(
            "json", methode="getGroupInfo", indata={"group_guid": guid_gap}, wn=self.cli
        )

    def getChannelInfo(self, guid_channel):
        return self.methods.methodsRubika(
            "json",
            methode="getChannelInfo",
            indata={"channel_guid": guid_channel},
            wn=self.cli,
        )

    def addMemberGroup(self, guid_gap, user_ids):
        return self.methods.methodsRubika(
            "json",
            methode="addGroupMembers",
            indata={"group_guid": guid_gap, "member_guids": user_ids},
            wn=self.cli,
        )

    def addMemberChannel(self, guid_channel, user_ids):
        return self.methods.methodsRubika(
            "json",
            methode="addChannelMembers",
            indata={"channel_guid": guid_channel, "member_guids": user_ids},
            wn=self.cli,
        )

    def getGroupAdmins(self, guid_gap):
        return self.methods.methodsRubika(
            "json",
            methode="getGroupAdminMembers",
            indata={"group_guid": guid_gap},
            wn=self.cli,
        )

    def getChannelAdmins(self, guid_channel):
        return self.methods.methodsRubika(
            "json",
            methode="getChannelAdminMembers",
            indata={"channel_guid": guid_channel},
            wn=self.cli,
        )

    def AddNumberPhone(self, first_num, last_num, numberPhone):
        return self.methods.methodsRubika(
            "json",
            methode="addAddressBook",
            indata={
                "phone": numberPhone,
                "first_name": first_num,
                "last_name": last_num,
            },
            wn=self.cli,
        )

    def getMessagesInfo(self, guid, message_ids: list):
        return self.methods.methodsRubika(
            "json",
            methode="getMessagesByID",
            indata={"object_guid": guid, "message_ids": message_ids},
            wn=self.cli,
        )

    def getGroupMembers(self, guid_gap, text=None, start_id=None):
        return self.methods.methodsRubika(
            "json",
            methode="getGroupAllMembers",
            indata={"group_guid": guid_gap, "search_text": text, "start_id": start_id},
            wn=self.cli,
        )

    def getChannelMembers(self, channel_guid, text=None, start_id=None):
        return self.methods.methodsRubika(
            "json",
            methode="getChannelAllMembers",
            indata={
                "channel_guid": channel_guid,
                "search_text": text,
                "start_id": start_id,
            },
            wn=self.cli,
        )

    def lockGroup(self, guid_gap):
        return self.methods.methodsRubika(
            "json",
            methode="setGroupDefaultAccess",
            indata={"access_list": ["AddMember"], "group_guid": guid_gap},
            wn=self.cli,
        )

    def unlockGroup(self, guid_gap):
        return self.methods.methodsRubika(
            "json",
            methode="setGroupDefaultAccess",
            indata={
                "access_list": ["SendMessages", "AddMember"],
                "group_guid": guid_gap,
            },
            wn=self.cli,
        )

    def getGroupLink(self, guid_gap):
        return self.methods.methodsRubika(
            "json", methode="getGroupLink", indata={"group_guid": guid_gap}, wn=self.cli
        )

    def numberOnline(self, guid_gap):
        return self.methods.methodsRubika(
            "json",
            methode="getGroupOnlineCount",
            indata={"group_guid": guid_gap},
            wn=self.cli,
        )

    def getChannelLink(self, guid_channel):
        return (
            self.methods.methodsRubika(
                "json",
                methode="getChannelLink",
                indata={"channel_guid": guid_channel},
                wn=self.cli,
            )
            .get("data")
            .get("join_link")
        )

    def changeGroupLink(self, guid_gap):
        return (
            self.methods.methodsRubika(
                "json",
                methode="setGroupLink",
                indata={"group_guid": guid_gap},
                wn=self.cli,
            )
            .get("data")
            .get("join_link")
        )

    def changeChannelLink(self, guid_channel):
        return (
            self.methods.methodsRubika(
                "json",
                methode="setChannelLink",
                indata={"channel_guid": guid_channel},
                wn=self.cli,
            )
            .get("data")
            .get("join_link")
        )

    def setGroupTimer(self, guid_gap, time):
        return self.methods.methodsRubika(
            "json",
            methode="editGroupInfo",
            indata={
                "group_guid": guid_gap,
                "slow_mode": time,
                "updated_parameters": ["slow_mode"],
            },
            wn=self.cli,
        )

    def setGroupAdmin(self, guid_gap, guid_member, access_admin=None):
        if access_admin == None:
            access_admin = (
                [
                    "ChangeInfo",
                    "SetJoinLink",
                    "SetAdmin",
                    "BanMember",
                    "DeleteGlobalAllMessages",
                    "PinMessages",
                    "SetMemberAccess",
                ]
                if access_admin == None
                else access_admin
            )
        return self.methods.methodsRubika(
            "json",
            methode="setGroupAdmin",
            indata={
                "group_guid": guid_gap,
                "access_list": access_admin,
                "action": "SetAdmin",
                "member_guid": guid_member,
            },
            wn=self.cli,
        )

    def deleteGroupAdmin(self, guid_gap, guid_admin):
        return self.methods.methodsRubika(
            "json",
            methode="setGroupAdmin",
            indata={
                "group_guid": guid_gap,
                "action": "UnsetAdmin",
                "member_guid": guid_admin,
            },
            wn=self.cli,
        )

    def deleteGroup(self, guid_gap):
        return self.methods.methodsRubika(
            "json", methode="removeGroup", indata={"group_guid": guid_gap}, wn=self.cli
        )

    def setChannelAdmin(self, guid_channel, guid_member, access_admin=None):
        if access_admin == None:
            access_admin = (
                [
                    "SetAdmin",
                    "SetJoinLink",
                    "AddMember",
                    "DeleteGlobalAllMessages",
                    "EditAllMessages",
                    "SendMessages",
                    "PinMessages",
                    "ViewAdmins",
                    "ViewMembers",
                    "ChangeInfo",
                ]
                if access_admin == None
                else access_admin
            )
        return self.methods.methodsRubika(
            "json",
            methode="setChannelAdmin",
            indata={
                "channel_guid": guid_channel,
                "access_list": access_admin,
                "action": "SetAdmin",
                "member_guid": guid_member,
            },
            wn=self.cli,
        )

    def deleteChannelAdmin(self, guid_channel, guid_admin):
        return self.methods.methodsRubika(
            "json",
            methode="setChannelAdmin",
            indata={
                "channel_guid": guid_channel,
                "action": "UnsetAdmin",
                "member_guid": guid_admin,
            },
            wn=self.cli,
        )

    def getStickersByEmoji(self, emojee):
        return (
            self.methods.methodsRubika(
                "json",
                methode="getStickersByEmoji",
                indata={"emoji_character": emojee, "suggest_by": "All"},
                wn=self.cli,
            )
            .get("data")
            .get("stickers")
        )

    def searchStickerSets(self, text, start_id=None):
        return self.methods.methodsRubika(
            "json",
            methode="searchStickerSets",
            indata={"search_text": text, "start_id": start_id},
            wn=self.cli,
        )

    def getTrendStickerSets(self, start_id=None):
        return self.methods.methodsRubika(
            "json",
            methode="getTrendStickerSets",
            indata={"start_id": start_id},
            wn=self.cli,
        )

    def getStickerSetByID(self, sticker_set_id=None):
        return self.methods.methodsRubika(
            "json",
            methode="getStickerSetByID",
            indata={"sticker_set_id": sticker_set_id},
            wn=self.cli,
        )

    def actionStickerSet(self, action: int, sticker_set_id=None):
        Action = ["Add", "Remove"]
        return self.methods.methodsRubika(
            "json",
            methode="actionOnStickerSet",
            indata={"sticker_set_id": sticker_set_id, "action": Action[action]},
            wn=self.cli,
        )

    def activenotification(self, guid):
        return self.methods.methodsRubika(
            "json",
            methode="setActionChat",
            indata={"action": "Unmute", "object_guid": guid},
            wn=self.cli,
        )

    def offnotification(self, guid):
        return self.methods.methodsRubika(
            "json",
            methode="setActionChat",
            indata={"action": "Mute", "object_guid": guid},
            wn=self.cli,
        )

    def sendPoll(self, guid, question, options: list):
        return self.methods.methodsRubika(
            "json",
            methode="createPoll",
            indata={
                "object_guid": guid,
                "options": options,
                "rnd": f"{randint(100000,999999999)}",
                "question": question,
                "type": "Regular",
                "is_anonymous": False,
                "allows_multiple_answers": True,
            },
            wn=self.cli,
        )

    def sendPollExam(self, guid, question, options: list, explanation):
        return self.methods.methodsRubika(
            "json",
            methode="createPoll",
            indata={
                "object_guid": guid,
                "options": options,
                "rnd": f"{randint(100000,999999999)}",
                "question": question,
                "type": "Quiz",
                "is_anonymous": False,
                "allows_multiple_answers": False,
                "explanation": explanation,
                "correct_option_index": 1,
            },
            wn=self.cli,
        )

    def getPollStatus(self, poll_id):
        return self.methods.methodsRubika(
            "json", methode="getPollStatus", indata={"poll_id": poll_id}, wn=self.cli
        )

    def getVoters(self, poll_id, index):
        return self.methods.methodsRubika(
            "json",
            methode="getPollOptionVoters",
            indata={"poll_id": poll_id, "selection_index": index},
            wn=self.cli,
        )

    def votePoll(self, poll_id, index):
        return self.methods.methodsRubika(
            "json",
            methode="votePoll",
            indata={"poll_id": poll_id, "selection_index": index},
            wn=self.cli,
        )

    def forwardMessages(self, From, message_ids, to):
        return self.methods.methodsRubika(
            "json",
            methode="forwardMessages",
            indata={
                "from_object_guid": From,
                "message_ids": message_ids,
                "rnd": f"{randint(100000,999999999)}",
                "to_object_guid": to,
            },
            wn=self.cli,
        )

    def VisitChatGroup(self, guid_gap):
        return self.methods.methodsRubika(
            "json",
            methode="editGroupInfo",
            indata={
                "chat_history_for_new_members": "Visible",
                "group_guid": guid_gap,
                "updated_parameters": ["chat_history_for_new_members"],
            },
            wn=self.cli,
        )

    def HideChatGroup(self, guid_gap):
        return self.methods.methodsRubika(
            "json",
            methode="editGroupInfo",
            indata={
                "chat_history_for_new_members": "Hidden",
                "group_guid": guid_gap,
                "updated_parameters": ["event_messages"],
            },
            wn=self.cli,
        )

    def pin(self, guid, message_id):
        return self.methods.methodsRubika(
            "json",
            methode="setPinMessage",
            indata={"action": "Pin", "message_id": message_id, "object_guid": guid},
            wn=self.cli,
        )

    def unpin(self, guid, message_id):
        return self.methods.methodsRubika(
            "json",
            methode="setPinMessage",
            indata={"action": "Unpin", "message_id": message_id, "object_guid": guid},
            wn=self.cli,
        )

    @property
    def logout(self):
        return self.methods.methodsRubika(
            "json", methode="logout", indata={}, wn=self.cli
        )

    def joinGroup(self, link):
        hashLink = link.split("/")[-1]
        return self.methods.methodsRubika(
            "json", methode="joinGroup", indata={"hash_link": hashLink}, wn=self.cli
        )

    def joinChannelAll(self, guid):
        if ("https://" or "http://") in guid:
            link = guid.split("/")[-1]
            return self.methods.methodsRubika(
                "json",
                methode="joinChannelByLink",
                indata={"hash_link": link},
                wn=self.cli,
            )
        elif "@" in guid or not "@" in guid:
            IDE = guid.replace("@", "")
            guid = self.getInfoByUsername(IDE)["data"]["channel"]["channel_guid"]
            return self.methods.methodsRubika(
                "json",
                methode="joinChannelAction",
                indata={"action": "Join", "channel_guid": guid},
                wn=self.cli,
            )
        elif guid.startswith("c0"):
            return self.methods.methodsRubika(
                "json",
                methode="joinChannelAction",
                indata={"action": "Join", "channel_guid": guid},
                wn=self.cli,
            )

    def joinChannelByLink(self, link):
        hashLink = link.split("/")[-1]
        return self.methods.methodsRubika(
            "json",
            methode="joinChannelByLink",
            indata={"hash_link": hashLink},
            wn=self.cli,
        )

    def joinChannelByID(self, ide):
        IDE = ide.replace("@", "")
        GUID = self.getInfoByUsername(IDE)["data"]["channel"]["channel_guid"]
        return self.methods.methodsRubika(
            "json",
            methode="joinChannelAction",
            indata={"action": "Join", "channel_guid": GUID},
            wn=self.cli,
        )

    def joinChannelByGuid(self, guid):
        return self.methods.methodsRubika(
            "json",
            methode="joinChannelAction",
            indata={"action": "Join", "channel_guid": guid},
            wn=self.cli,
        )

    def leaveGroup(self, guid_gap):
        if "https://" in guid_gap:
            guid_gap = self.joinGroup(guid_gap)["data"]["group"]["group_guid"]
        else:
            guid_gap = guid_gap
        return self.methods.methodsRubika(
            "json", methode="leaveGroup", indata={"group_guid": guid_gap}, wn=self.cli
        )

    def leaveChannel(self, guid_channel):
        if "https://" in guid_channel:
            guid_channel = self.joinChannelByLink(guid_channel)["data"]["chat_update"][
                "object_guid"
            ]
        elif "@" in guid_channel:
            guid_channel = self.joinChannelByID(guid_channel)["data"]["chat_update"][
                "object_guid"
            ]
        else:
            guid_channel = guid_channel
        return self.methods.methodsRubika(
            "json",
            methode="joinChannelAction",
            indata={"action": "Leave", "channel_guid": guid_channel},
            wn=self.cli,
        )

    def EditNameGroup(self, groupgu, namegp, biogp=None):
        return self.methods.methodsRubika(
            "json",
            methode="editGroupInfo",
            indata={
                "description": biogp,
                "group_guid": groupgu,
                "title": namegp,
                "updated_parameters": ["title", "description"],
            },
            wn=self.cli,
        )

    def EditBioGroup(self, groupgu, biogp, namegp=None):
        return self.methods.methodsRubika(
            "json",
            methode="editGroupInfo",
            indata={
                "description": biogp,
                "group_guid": groupgu,
                "title": namegp,
                "updated_parameters": ["title", "description"],
            },
            wn=self.cli,
        )

    def block(self, guid_user):
        return self.methods.methodsRubika(
            "json",
            methode="setBlockUser",
            indata={"action": "Block", "user_guid": guid_user},
            wn=self.cli,
        )

    def unblock(self, guid_user):
        return self.methods.methodsRubika(
            "json",
            methode="setBlockUser",
            indata={"action": "Unblock", "user_guid": guid_user},
            wn=self.cli,
        )

    def startVoiceChat(self, guid):
        return self.methods.methodsRubika(
            "json",
            methode="createGroupVoiceChat",
            indata={"chat_guid": guid},
            wn=self.cli,
        )

    def addUserContact(self, guid):
        return self.methods.methodsRubika(
            "json",
            methode="setAskSpamAction",
            indata={"object_guid": guid, "action": "AddToContact"},
            wn=self.cli,
        )

    def getGroupVoiceChat(self, guid_gap):
        voice_chat_id = self.getGroupInfo(guid_gap)["data"]["chat"][
            "group_voice_chat_id"
        ]
        return self.methods.methodsRubika(
            "json",
            methode="getGroupVoiceChat",
            indata={"voice_chat_id": voice_chat_id, "chat_guid": guid_gap},
            wn=self.cli,
        )

    def getGroupVoiceChatParticipants(self, guid_gap, start_id=None):
        voice_chat_id = self.getGroupInfo(guid_gap)["data"]["chat"][
            "group_voice_chat_id"
        ]
        return self.methods.methodsRubika(
            "json",
            methode="getGroupVoiceChatParticipants",
            indata={
                "chat_guid": guid_gap,
                "voice_chat_id": voice_chat_id,
                "start_id": start_id,
            },
            wn=self.cli,
        )

    #  join_muted = true  Members can speak join_muted = false Members can not speak
    def editVoiceChat(self, guid, bol):
        voice_chat_id = self.getGroupInfo(guid)["data"]["chat"]["group_voice_chat_id"]
        return self.methods.methodsRubika(
            "json",
            methode="setGroupVoiceChatSetting",
            indata={
                "chat_guid": guid,
                "voice_chat_id": voice_chat_id,
                "join_muted": bol,
                "updated_parameters": ["join_muted"],
            },
            wn=self.cli,
        )

    def changeTitleVoiceChat(self, guid, title):
        voice_chat_id = self.getGroupInfo(guid)["data"]["chat"]["group_voice_chat_id"]
        return self.methods.methodsRubika(
            "json",
            methode="setGroupVoiceChatSetting",
            indata={
                "chat_guid": guid,
                "voice_chat_id": voice_chat_id,
                "title": title,
                "updated_parameters": ["title"],
            },
            wn=self.cli,
        )

    def finishVoiceChat(self, guid):
        voice_chat_id = self.getGroupInfo(guid)["data"]["chat"]["group_voice_chat_id"]
        return self.methods.methodsRubika(
            "json",
            methode="discardGroupVoiceChat",
            indata={"chat_guid": guid, "voice_chat_id": voice_chat_id},
            wn=self.cli,
        )

    def leaveGroupVoiceChat(self, guid):
        voice_chat_id = self.getGroupInfo(guid)["data"]["chat"]["group_voice_chat_id"]
        return self.methods.methodsRubika(
            "json",
            methode="leaveGroupVoiceChat",
            indata={"chat_guid": guid, "voice_chat_id": voice_chat_id},
            wn=self.cli,
        )

    def getDisplayAsInGroupVoiceChat(self, guid_gap, start_id=None):
        return self.methods.methodsRubika(
            "json",
            methode="getDisplayAsInGroupVoiceChat",
            indata={"chat_guid": guid_gap, "start_id": start_id},
            wn=self.cli,
        )

    def sendGroupVoiceChatActivity(self, guid_gap, model):
        return self.methods.methodsRubika(
            "json",
            methode="sendGroupVoiceChatActivity",
            indata={"try_count": guid_gap, "model": model},
            wn=self.cli,
        )

    def getGroupVoiceChatUpdates(self, guid_gap, state):
        voice_chat_id = self.getGroupInfo(guid_gap)["data"]["chat"][
            "group_voice_chat_id"
        ]
        return self.methods.methodsRubika(
            "json",
            methode="getGroupVoiceChatUpdates",
            indata={
                "chat_guid": guid_gap,
                "voice_chat_id": voice_chat_id,
                "state": state,
            },
            wn=self.cli,
        )

    def getUserInfo(self, guid_user):
        return self.methods.methodsRubika(
            "json", methode="getUserInfo", indata={"user_guid": guid_user}, wn=self.cli
        )

    def getUserInfoByIDE(self, IDE_user):
        guiduser = self.getInfoByUsername(IDE_user.replace("@", ""))["data"]["user"][
            "user_guid"
        ]
        return self.methods.methodsRubika(
            "json", methode="getUserInfo", indata={"user_guid": guiduser}, wn=self.cli
        )

    def seeGroupbyLink(self, link_gap):
        link = link_gap.replace("https://rubika.ir/joing/", "")
        return self.methods.methodsRubika(
            "json",
            methode="groupPreviewByJoinLink",
            indata={"hash_link": link},
            wn=self.cli,
        ).get("data")

    def seeChannelbyLink(self, link_channel):
        link = link_channel.replace("https://rubika.ir/joinc/", "")
        return self.methods.methodsRubika(
            "json",
            methode="channelPreviewByJoinLink",
            indata={"hash_link": link},
            wn=self.cli,
        ).get("data")

    def getAvatars(self, guid):
        return self.methods.methodsRubika(
            "json", methode="getAvatars", indata={"object_guid": guid}, wn=self.cli
        )

    def uploadAvatar_replay(self, guid, files_ide):
        return self.methods.methodsRubika(
            "json",
            methode="uploadAvatar",
            indata={
                "object_guid": guid,
                "thumbnail_file_id": files_ide,
                "main_file_id": files_ide,
            },
            wn=self.cli,
        )

    def uploadAvatar(self, guid, main, thumbnail=None):
        mainID = str(self.Upload.uploadFile(main)[0]["id"])
        thumbnailID = str(self.Upload.uploadFile(thumbnail or main)[0]["id"])
        return self.methods.methodsRubika(
            "json",
            methode="uploadAvatar",
            indata={
                "object_guid": guid,
                "thumbnail_file_id": thumbnailID,
                "main_file_id": mainID,
            },
            wn=self.cli,
        )

    def removeAvatar(self, guid):
        avatar_id = self.getAvatars(guid)["data"]["avatars"][0]["avatar_id"]
        return self.methods.methodsRubika(
            "json",
            methode="deleteAvatar",
            indata={"object_guid": guid, "avatar_id": avatar_id},
            wn=self.cli,
        )

    def removeAllAvatars(self, guid):
        while 1:
            try:
                avatar = self.getAvatars(guid)["data"]["avatars"]
                if avatar != []:
                    avatar_id = self.getAvatars(guid)["data"]["avatars"][0]["avatar_id"]
                    self.methods.methodsRubika(
                        "json",
                        methode="deleteAvatar",
                        indata={"object_guid": guid, "avatar_id": avatar_id},
                        wn=self.cli,
                    )
                else:
                    return "Ok remove Avatars"
                    break
            except:
                continue

    def Devicesrubika(self, service_guid):
        return self.methods.methodsRubika(
            "json",
            methode="getServiceInfo",
            indata={"service_guid": service_guid},
            wn=self.cli,
        )

    def deleteChatHistory(self, guid, last_message_id):
        return self.methods.methodsRubika(
            "json",
            methode="deleteChatHistory",
            indata={"last_message_id": last_message_id, "object_guid": guid},
            wn=self.cli,
        )

    def addFolder(
        self,
        Name="Arsein",
        include_chat=None,
        include_object=None,
        exclude_chat=None,
        exclude_object=None,
    ):
        return self.methods.methodsRubika(
            "json",
            methode="addFolder",
            indata={
                "exclude_chat_types": exclude_chat,
                "exclude_object_guids": exclude_object,
                "include_chat_types": include_chat,
                "include_object_guids": include_object,
                "is_add_to_top": True,
                "name": Name,
            },
            wn=self.cli,
        )

    def deleteFolder(self, folder_id):
        return self.methods.methodsRubika(
            "json", methode="deleteFolder", indata={"folder_id": folder_id}, wn=self.cli
        )

    def addGroup(self, title, guidsUser: list):
        return self.methods.methodsRubika(
            "json",
            methode="addGroup",
            indata={"member_guids": guidsUser, "title": title},
            wn=self.cli,
        )

    def deleteGroup(self, guid_group):
        return self.methods.methodsRubika(
            "json",
            methode="deleteNoAccessGroupChat",
            indata={"group_guid": guid_group},
            wn=self.cli,
        )

    def addChannel(self, title, typeChannell: int, bio, guidsUser: list):
        TypeChannell = ["Private", "Public"]
        return self.methods.methodsRubika(
            "json",
            methode="addChannel",
            indata={
                "channel_type": TypeChannell[typeChannell],
                "description": bio,
                "member_guids": guidsUser,
                "title": title,
            },
            wn=self.cli,
        )

    def breturn(self, start_id=None):
        return self.methods.methodsRubika(
            "json",
            methode="getBreturnUsers",
            indata={"start_id": start_id},
            wn=self.cli,
        )

    def editUser(self, first_name=None, last_name=None, bio=None):
        return self.methods.methodsRubika(
            "json",
            methode="updateProfile",
            indata={
                "bio": bio,
                "first_name": first_name,
                "last_name": last_name,
                "updated_parameters": ["first_name", "last_name", "bio"],
            },
            wn=self.cli,
        )

    def editusername(self, username):
        ide = username.replace("@", "")
        return self.methods.methodsRubika(
            "json", methode="updateUsername", indata={"username": ide}, wn=self.cli
        )

    def Postion(self, guid, guiduser):
        return self.methods.methodsRubika(
            "json",
            methode="requestChangeObjectOwner",
            indata={"new_owner_user_guid": guiduser, "object_guid": guid},
            wn=self.cli,
        )

    def getPostion(self, guid):
        return self.methods.methodsRubika(
            "json",
            methode="getPendingObjectOwner",
            indata={"object_guid": guid},
            wn=self.cli,
        )

    def AcceptPostion(self, guid):
        return self.methods.methodsRubika(
            "json",
            methode="replyRequestObjectOwner",
            indata={"action": "Accept", "object_guid": guid},
            wn=self.cli,
        )

    def RejectPostion(self, guid):
        return self.methods.methodsRubika(
            "json",
            methode="replyRequestObjectOwner",
            indata={"action": "Reject", "object_guid": guid},
            wn=self.cli,
        )

    def sendLive(self, guid, titlelive):
        return self.methods.methodsRubika(
            "json",
            methode="sendLive",
            indata={
                "object_guid": guid,
                "title": titlelive,
                "device_type": "Software",
                "thumb_inline": self.thumb_inline,
                "rnd": randint(100000, 999999),
            },
            wn=self.cli,
        )

    @property
    def ClearAccounts(self):
        return self.methods.methodsRubika(
            "json", methode="terminateOtherSessions", indata={}, wn=self.cli
        )

    @property
    def DeleteAccount(self):
        return self.methods.methodsRubika(
            "json", methode="requestDeleteAccount", indata={}, wn=self.cli
        )

    def selectionClearAccount(self, session_key):
        return self.methods.methodsRubika(
            "json",
            methode="terminateSession",
            indata={"session_key": session_key},
            wn=self.cli,
        )

    def HidePhone(self, **kwargs):
        return self.methods.methodsRubika(
            "json",
            methode="setSetting",
            indata={"settings": kwargs, "update_parameters": ["show_my_phone_number"]},
            wn=self.cli,
        )

    def HideOnline(self, **kwargs):
        return self.methods.methodsRubika(
            "json",
            methode="setSetting",
            indata={"settings": kwargs, "update_parameters": ["show_my_last_online"]},
            wn=self.cli,
        )

    def search_inaccount(self, text):
        return (
            self.methods.methodsRubika(
                "json",
                methode="searchGlobalMessages",
                indata={"search_text": text, "start_id": None, "type": "Text"},
                wn=self.cli,
            )
            .get("data")
            .get("messages")
        )

    def search_inrubika(self, text):
        return (
            self.methods.methodsRubika(
                "json",
                methode="searchGlobalObjects",
                indata={"search_text": text},
                wn=self.cli,
            )
            .get("data")
            .get("objects")
        )

    def getAbsObjects(self, guids: list):
        return self.methods.methodsRubika(
            "json",
            methode="getAbsObjects",
            indata={"objects_guids": guids},
            wn=self.cli,
        )

    def Infolinkpost(self, linkpost):
        return self.methods.methodsRubika(
            "json",
            methode="getLinkFromAppUrl",
            indata={"app_url": linkpost},
            wn=self.cli,
        )

    def addToMyGifSet(self, guid, message_id):
        return self.methods.methodsRubika(
            "json",
            methode="addToMyGifSet",
            indata={"message_id": message_id, "object_guid": guid},
            wn=self.cli,
        )

    def deleteMyGifSet(self, file_id):
        return self.methods.methodsRubika(
            "json",
            methode="removeFromMyGifSet",
            indata={"file_id": file_id},
            wn=self.cli,
        )

    def getContactsLastOnline(self, user_guids: list):
        return self.methods.methodsRubika(
            "json",
            methode="getContactsLastOnline",
            indata={"user_guids": user_guids},
            wn=self.cli,
        )

    def SignMessageChannel(self, guid_channel, sign: bool):
        return self.methods.methodsRubika(
            "json",
            methode="editChannelInfo",
            indata={
                "channel_guid": guid_channel,
                "sign_messages": sign,
                "updated_parameters": ["sign_messages"],
            },
            wn=self.cli,
        )

    @property
    def ActiveContectJoin(self):
        return self.methods.methodsRubika(
            "json",
            methode="setSetting",
            indata={
                "settings": {"can_join_chat_by": "MyContacts"},
                "update_parameters": ["can_join_chat_by"],
            },
            wn=self.cli,
        )

    @property
    def ActiveEverybodyJoin(self):
        return self.methods.methodsRubika(
            "json",
            methode="setSetting",
            indata={
                "settings": {"can_join_chat_by": "Everybody"},
                "update_parameters": ["can_join_chat_by"],
            },
            wn=self.cli,
        )

    def CalledBy(self, typeCall: str):
        return self.methods.methodsRubika(
            "json",
            methode="setSetting",
            indata={
                "settings": {"can_called_by": typeCall},
                "update_parameters": ["can_called_by"],
            },
            wn=self.cli,
        )

    def changeChannelID(self, guid_channel, username):
        return self.methods.methodsRubika(
            "json",
            methode="updateChannelUsername",
            indata={
                "channel_guid": guid_channel,
                "username": username.replace("@", ""),
            },
            wn=self.cli,
        )

    def getMessageShareUrl(self, guid, messageId):
        return self.methods.methodsRubika(
            "json",
            methode="getMessageShareUrl",
            indata={"object_guid": guid, "messageId": messageId},
            wn=self.cli,
        )

    def getBlockedUsers(self, start_id=None):
        return self.methods.methodsRubika(
            "json",
            methode="getBlockedUsers",
            indata={"start_id": start_id},
            wn=self.cli,
        )

    def deleteContact(self, guid_user):
        return self.methods.methodsRubika(
            "json",
            methode="deleteContact",
            indata={"user_guid": guid_user},
            wn=self.cli,
        )

    def checkUserUsername(self, username):
        return self.methods.methodsRubika(
            "json",
            methode="checkUserUsername",
            indata={"username": username.replace("@", "")},
            wn=self.cli,
        )

    def checkChannelUsername(self, username):
        return self.methods.methodsRubika(
            "json",
            methode="checkChannelUsername",
            indata={"username": username.replace("@", "")},
            wn=self.cli,
        )

    def getContacts(self, start_id=None):
        return self.methods.methodsRubika(
            "json", methode="getContacts", indata={"start_id": start_id}, wn=self.cli
        )

    def getLiveStatus(self, live_id, token_live):
        return self.methods.methodsRubika(
            "json",
            methode="getLiveStatus",
            indata={"live_id": live_id, "access_token": token_live},
            wn=self.cli,
        )

    def getLiveComments(self, live_id, token_live):
        return self.methods.methodsRubika(
            "json",
            methode="getLiveComments",
            indata={"live_id": live_id, "access_token": token_live},
            wn=self.cli,
        )

    @property
    def getdatabaseReaction(self):
        return self.methods.methodsRubika(
            "json", methode="getAvailableReactions", indata={}, wn=self.cli
        )

    def Reaction(self, guid, typeReaction, reaction, message_id):
        if typeReaction == "add":
            return self.methods.methodsRubika(
                "json",
                methode="actionOnMessageReaction",
                indata={
                    "action": "Add",
                    "reaction_id": reaction,
                    "message_id": message_id,
                    "object_guid": guid,
                },
                wn=self.cli,
            )
        elif typeReaction == "remove":
            return self.methods.methodsRubika(
                "json",
                methode="actionOnMessageReaction",
                indata={
                    "action": "Remove",
                    "reaction_id": reaction,
                    "message_id": message_id,
                    "object_guid": guid,
                },
                wn=self.cli,
            )

    def commonGroup(self, guid_user):
        IDE = guid_user.replace("@", "")
        GUID = self.getInfoByUsername(IDE)["data"]["user"]["user_guid"]
        return self.methods.methodsRubika(
            "json", methode="getCommonGroups", indata={"user_guid": GUID}, wn=self.cli
        )

    def setTypeChannel(self, guid_channel, type_Channel):
        if type_Channel == "Private":
            return self.methods.methodsRubika(
                "json",
                methode="editChannelInfo",
                indata={
                    "channel_guid": guid_channel,
                    "channel_type": "Private",
                    "updated_parameters": ["channel_type"],
                },
                wn=self.cli,
            )
        else:
            if type_Channel == "Public":
                return self.methods.methodsRubika(
                    "json",
                    methode="editChannelInfo",
                    indata={
                        "settings": {
                            "channel_guid": guid_channel,
                            "channel_type": "Public",
                            "updated_parameters": ["channel_type"],
                        }
                    },
                    wn=self.cli,
                )

    def getChatAds(self, user_guids: list):
        state = str(round(datetime.datetime.today().timestamp()) - 200)
        return self.methods.methodsRubika(
            "json", methode="getChatAds", indata={"state": state}, wn=self.cli
        )

    def clickMessageUrl(self, guid, message_id, link):
        return self.methods.methodsRubika(
            "json",
            methode="clickMessageUrl",
            indata={"object_guid": guid, "message_id": message_id, "link_url": link},
            wn=self.cli,
        )

    def seenChat(self, guid, message_id):
        return self.methods.methodsRubika(
            "json",
            methode="seenChat",
            indata={"seen_list": {f"{guid}": f"{message_id}"}},
            wn=self.cli,
        )

    @property
    def getContactsUpdates(self):
        state = str(round(datetime.datetime.today().timestamp()) - 200)
        return self.methods.methodsRubika(
            "json", methode="getContactsUpdates", indata={"state": state}, wn=self.cli
        )

    def twolocks(self, ramz, hide):
        locked = self.methods.methodsRubika(
            "json",
            methode="setupTwoStepVerification",
            indata={"hint": hide, "password": ramz},
            wn=self.cli,
        )
        if locked["status"] == "ERROR_GENERIC":
            return locked["self.client_show_message"]["link"]["alert_data"]["message"]
        else:
            return locked

    def deletetwolocks(self, password):
        return self.methods.methodsRubika(
            "json", methode="turnOffTwoStep", indata={"password": password}, wn=self.cli
        )

    def checkPassword(self, password):
        return self.methods.methodsRubika(
            "json",
            methode="checkTwoStepPasscode",
            indata={"password": password},
            wn=self.cli,
        )

    def passwordChange(self, password):
        return self.methods.methodsRubika(
            "json",
            methode="resendCodeRecoveryEmail",
            indata={"password": password},
            wn=self.cli,
        )

    def loginforgetPassword(self, emailCode, password, phone_number):
        return self.methods.methodsRubika(
            "json",
            methode="loginDisableTwoStep",
            indata={
                "email_code": emailCode,
                "forget_password_code_hash": password,
                "phone_number": phone_number,
            },
            wn=self.cli,
        )

    def ProfileEdit(self, first_name=None, last_name=None, bio=None, username=None):
        while 1:
            try:
                for tekrar in range(1):
                    self.editUser(first_name=first_name, last_name=last_name, bio=bio)
                    self.editusername(username.replace("@", ""))
                    return "Profile edited"
                break
            except:
                continue

    def getChatGroup(self, guid_gap):
        while 1:
            try:
                for tekrar in range(1):
                    lastmessages = self.getGroupInfo(guid_gap)["data"]["chat"][
                        "last_message_id"
                    ]
                    messages = self.getMessages(guid_gap, lastmessages)
                    return messages
                break
            except:
                continue

    def getChatChannel(self, guid_channel):
        while 1:
            try:
                for tekrar in range(1):
                    lastmessages = self.getChannelInfo(guid_channel)["data"]["chat"][
                        "last_message_id"
                    ]
                    messages = self.getMessages(guid_channel, lastmessages)
                    return messages
                break
            except:
                continue

    def getChatUser(self, guid_User):
        while 1:
            try:
                for tekrar in range(1):
                    lastmessages = self.getUserInfo(guid_User)["data"]["chat"][
                        "last_message_id"
                    ]
                    messages = self.getMessages(guid_User, lastmessages)
                    return messages
                break
            except:
                continue

    @property
    def Authrandom(self):
        auth = ""
        meghdar = "qwertyuiopasdfghjklzxcvbnm0123456789"
        for string in range(32):
            auth += choice(meghdar)
        return auth

    # method send Files

    def requestSendFile(self, addressfile):
        return self.methods.methodsRubika(
            "json",
            methode="requestSendFile",
            indata={
                "file_name": os.path.basename(addressfile),
                "size": os.path.getsize(addressfile),
                "mime": os.path.splitext(addressfile)[1].strip("."),
            },
            wn=self.cli,
        )

    def sender(self, guid, message_id: list):
        datamsg = self.getMessagesInfo(guid, message_id).get("data").get("messages")[0]
        resend = makeJsonResend(guid, datamsg.get("file_inline"))
        if "text" in datamsg.keys():
            resend["text"] = datamsg.get("text")
        else:
            resend["text"] = None
        return self.methods.methodsRubika(
            "json", methode="sendMessage", indata=resend, wn=self.cli
        )

    def downloadFiles(self, guid, message_id: list, link=False):
        getdatafile = (
            self.getMessagesInfo(guid, message_id)
            .get("data")
            .get("messages")[0]
            .get("file_inline")
        )
        if link == False:
            return self.methods.methodsRubika(
                "download",
                downloads=[
                    self.Auth,
                    getdatafile.get("dc_id"),
                    getdatafile.get("file_id"),
                    getdatafile.get("size"),
                    getdatafile.get("access_hash_rec"),
                ],
            )
        elif link == True:
            Link: str = (
                f"https://messenger{getdatafile.get('dc_id')}.iranlms.ir/InternFile.ashx?id={getdatafile.get('file_id')}&ach={getdatafile.get('access_hash_rec')}"
            )
            file: bin = httpx.get(Link).content
            return [file, True]

    def Http(self, link, formats):
        while True:
            try:
                for tek in range(1):

                    async def download_file(link, formatt):
                        async with aiohttp.ClientSession() as session:
                            async with session.get(link) as response:
                                if response.status == 200:
                                    while True:
                                        buildnamefiles = f"LibraryArseinRubika{randint(0,1000)}.{formatt}"
                                        checkname = os.path.exists(buildnamefiles)
                                        if checkname == False:
                                            for tek in range(1):
                                                with open(buildnamefiles, "wb") as file:
                                                    content = await response.read()
                                                    file.write(content)
                                                return buildnamefiles
                                            break
                                        else:
                                            continue
                                else:
                                    return 404

                    loop = asyncio.get_event_loop()
                    return loop.run_until_complete(download_file(link, formats))
                break
            except Exception as Error:
                continue

    def SendSticker(
        self,
        guid,
        emoji_character,
        w_h_ratio,
        sticker_id,
        file_id,
        dc_id,
        access_hash_rec,
        sticker_set_id,
    ):
        return self.methods.methodsRubika(
            "json",
            methode="sendMessage",
            indata={
                "object_guid": guid,
                "rnd": randint(100000, 999999999),
                "sticker": {
                    "emoji_character": emoji_character,
                    "w_h_ratio": w_h_ratio,
                    "sticker_id": sticker_id,
                    "file": {
                        "file_id": file_id,
                        "mime": "png",
                        "dc_id": dc_id,
                        "access_hash_rec": access_hash_rec,
                        "file_name": "sticker.png",
                        "cdn_tag": "PR5",
                        "size": 0,
                    },
                    "sticker_set_id": sticker_set_id,
                },
            },
            wn=self.cli,
        )

    def SendImage(
        self,
        guid,
        addressfile,
        spoil: bool = False,
        thumbinline=None,
        caption=None,
        message_id=None,
    ):
        addressfile: str = (
            addressfile
            if not addressfile.startswith("https://" or "http://")
            else self.Http(addressfile, "png")
        )
        if addressfile != 404 and os.path.exists(addressfile):
            getSize = str(os.path.getsize(addressfile))
            getphoto = Image.open(addressfile)
            up = self.Upload.uploadFile(addressfile)
            width, height = getphoto.size
            thumbinline = (
                self.thumb_inline
                if thumbinline == None
                else str(getThumbInline(open(addressfile, "rb").read()))
            )
            getphoto.close()
            if addressfile.startswith("LibraryArseinRubika"):
                os.remove(addressfile)
            return self.methods.methodsRubika(
                "json",
                methode="sendMessage",
                indata={
                    "object_guid": guid,
                    "rnd": randint(100000, 999999999),
                    "file_inline": {
                        "dc_id": up[0]["dc_id"],
                        "file_id": up[0]["id"],
                        "type": "Image",
                        "file_name": os.path.basename(addressfile),
                        "size": getSize,
                        "is_spoil": spoil,
                        "mime": os.path.splitext(addressfile)[1].strip("."),
                        "thumb_inline": thumbinline,
                        "width": width,
                        "height": height,
                        "access_hash_rec": up[1],
                    },
                    "text": caption,
                    "reply_to_message_id": message_id,
                },
                wn=self.cli,
            )
        else:
            return "error sendPhoto"

    def SendFile(self, guid, addressfile, formats=None, caption=None, message_id=None):
        addressfile = (
            addressfile
            if not addressfile.startswith("https://" or "http://")
            else self.Http(addressfile, formats)
        )
        if addressfile != 404 and os.path.exists(addressfile):
            getSize = str(os.path.getsize(addressfile))
            up = self.Upload.uploadFile(addressfile)
            if addressfile.startswith("LibraryArseinRubika"):
                os.remove(addressfile)
            return self.methods.methodsRubika(
                "json",
                methode="sendMessage",
                indata={
                    "object_guid": guid,
                    "rnd": randint(100000, 999999999),
                    "file_inline": {
                        "dc_id": up[0]["dc_id"],
                        "file_id": up[0]["id"],
                        "type": "File",
                        "file_name": os.path.basename(addressfile),
                        "size": getSize,
                        "mime": os.path.splitext(addressfile)[1].strip("."),
                        "access_hash_rec": up[1],
                    },
                    "text": caption,
                    "reply_to_message_id": message_id,
                },
                wn=self.cli,
            )
        else:
            return "error SendFile"

    def SendVideo(
        self,
        guid,
        addressfile,
        spoil: bool = False,
        breadth=None,
        thumbinline=None,
        caption=None,
        message_id=None,
    ):
        addressfile = (
            addressfile
            if not addressfile.startswith("https://" or "http://")
            else self.Http(addressfile, "mp4")
        )
        if addressfile != 404 and os.path.exists(addressfile):
            getSize = str(os.path.getsize(addressfile))
            getvideo = TinyTag.get(addressfile)
            width, height = [100, 100]
            up = self.Upload.uploadFile(addressfile)
            thumbinline = (
                self.thumb_inline
                if thumbinline == None
                else str(getThumbInline(open(addressfile, "rb").read()))
            )
            if addressfile.startswith("LibraryArseinRubika"):
                os.remove(addressfile)
            return self.methods.methodsRubika(
                "json",
                methode="sendMessage",
                indata={
                    "object_guid": guid,
                    "rnd": randint(100000, 999999999),
                    "file_inline": {
                        "dc_id": up[0]["dc_id"],
                        "file_id": up[0]["id"],
                        "type": "Video",
                        "file_name": os.path.basename(addressfile),
                        "size": getSize,
                        "is_spoil": spoil,
                        "mime": os.path.splitext(addressfile)[1].strip("."),
                        "thumb_inline": thumbinline,
                        "width": width,
                        "height": height,
                        "time": int(getvideo.duration * 1000),
                        "access_hash_rec": up[1],
                    },
                    "text": caption,
                    "reply_to_message_id": message_id,
                },
                wn=self.cli,
            )
        else:
            return "error SendVideo"

    def SendGif(
        self,
        guid,
        addressfile,
        breadth=None,
        thumbinline=None,
        caption=None,
        message_id=None,
    ):
        addressfile = (
            addressfile
            if not addressfile.startswith("https://" or "http://")
            else self.Http(addressfile, "mp4")
        )
        if addressfile != 404 and os.path.exists(addressfile):
            getSize = str(os.path.getsize(addressfile))
            getvideo = TinyTag.get(addressfile)
            width, height = [100, 100]
            up = self.Upload.uploadFile(addressfile)
            thumbinline = (
                self.thumb_inline
                if thumbinline == None
                else str(getThumbInline(open(addressfile, "rb").read()))
            )
            if addressfile.startswith("LibraryArseinRubika"):
                os.remove(addressfile)
            return self.methods.methodsRubika(
                "json",
                methode="sendMessage",
                indata={
                    "file_inline": {
                        "access_hash_rec": up[1],
                        "auto_play": False,
                        "dc_id": up[0]["dc_id"],
                        "file_id": up[0]["id"],
                        "file_name": os.path.basename(addressfile),
                        "height": height,
                        "mime": os.path.splitext(addressfile)[1].strip("."),
                        "size": getSize,
                        "thumb_inline": thumbinline,
                        "time": int(getvideo.duration * 1000),
                        "type": "Gif",
                        "width": width,
                    },
                    "is_mute": False,
                    "object_guid": guid,
                    "rnd": randint(100000, 999999999),
                    "text": caption,
                    "reply_to_message_id": message_id,
                },
                wn=self.cli,
            )
        else:
            return "error SendGif"

    def SendVoice(
        self, guid, addressfile, timevoice=None, caption=None, message_id=None
    ):
        addressfile = (
            addressfile
            if not addressfile.startswith("https://" or "http://")
            else self.Http(addressfile, "mp3")
        )
        if addressfile != 404 and os.path.exists(addressfile):
            getSize = str(os.path.getsize(addressfile))
            getMP3 = MP3(addressfile)
            time = getMP3.info.length if timevoice == None else timevoice
            up = self.Upload.uploadFile(addressfile)
            if addressfile.startswith("LibraryArseinRubika"):
                os.remove(addressfile)
            return self.methods.methodsRubika(
                "json",
                methode="sendMessage",
                indata={
                    "file_inline": {
                        "dc_id": up[0]["dc_id"],
                        "file_id": up[0]["id"],
                        "type": "Voice",
                        "file_name": os.path.basename(addressfile),
                        "size": getSize,
                        "time": time,
                        "mime": os.path.splitext(addressfile)[1].strip("."),
                        "access_hash_rec": up[1],
                    },
                    "object_guid": guid,
                    "rnd": f"{randint(100000,999999999)}",
                    "text": caption,
                    "reply_to_message_id": message_id,
                },
                wn=self.cli,
            )
        else:
            return "error SendVoice"

    def SendMusic(self, guid, addressfile, caption=None, message_id=None):
        addressfile = (
            addressfile
            if not addressfile.startswith("https://" or "http://")
            else self.Http(addressfile, "mp3")
        )
        if addressfile != 404 and os.path.exists(addressfile):
            getSize = str(os.path.getsize(addressfile))
            getMP3 = MP3(addressfile)
            width, height, time = (
                getMP3.info.channels,
                getMP3.info.sample_rate,
                getMP3.info.length,
            )
            up = self.Upload.uploadFile(addressfile)
            if addressfile.startswith("LibraryArseinRubika"):
                os.remove(addressfile)
            return self.methods.methodsRubika(
                "json",
                methode="sendMessage",
                indata={
                    "file_inline": {
                        "access_hash_rec": up[1],
                        "auto_play": False,
                        "dc_id": up[0]["dc_id"],
                        "file_id": up[0]["id"],
                        "file_name": os.path.basename(addressfile),
                        "height": height,
                        "mime": os.path.splitext(addressfile)[1].strip("."),
                        "music_performer": "library ArseinRubika",
                        "size": getSize,
                        "time": time,
                        "type": "Music",
                        "width": width,
                    },
                    "is_mute": False,
                    "object_guid": guid,
                    "rnd": randint(100000, 999999999),
                    "text": caption,
                    "reply_to_message_id": message_id,
                },
                wn=self.cli,
            )
        else:
            return "error SendMusic"

    # method logins

    @property
    def register(self):
        if self.TypePlatform == "web":
            return self.methods.methodsRubika(
                "json",
                methode="registerDevice",
                indata=DeviceTelephone.DeviceWeb,
                wn=self.cli,
            )
        elif self.TypePlatform == "android":
            return self.methods.methodsRubika(
                "json",
                methode="registerDevice",
                indata=DeviceTelephone.DeviceAndroid,
                wn=self.cli,
            )


@staticmethod
def sendCode(platforms, numberphone: str, send_type: bool = False, password=None):
    cli, method = clien(platforms).platform, method_Rubika()
    send_type = "Internal" if send_type != False else "SMS"
    return method.methodsRubika(
        "login",
        methode="sendCode",
        indata={
            "phone_number": f"98{numberphone[1:]}",
            "send_type": send_type,
            "pass_key": password,
        },
        wn=cli,
    )


@staticmethod
def signIn(platforms, numberphone: str, codehash, phone_code, save=None):
    publicKey, privateKey = encoderjson.rsaKeyGenerate()
    method, cli = method_Rubika(), clien(platforms).platform
    if platforms and numberphone and codehash and phone_code:
        GetDataSignIn = method.methodsRubika(
            "login",
            methode="signIn",
            indata={
                "phone_number": f"98{numberphone[1:]}",
                "phone_code_hash": codehash,
                "phone_code": phone_code,
                "public_key": publicKey,
                "private_key": privateKey,
            },
            wn=cli,
        )
        if GetDataSignIn.get("data").get("status") == "OK":
            data_account = dict(
                Auth=encoderjson.decryptRsaOaep(
                    privateKey, GetDataSignIn.get("data").get("auth")
                ),
                Key=privateKey,
            )
            if save != None:
                with open(f"{save}.json", "w") as f:
                    json.dump(data_account, f)
            return data_account

        elif GetDataSignIn.get("data").get("status") == "CodeIsInvalid":
            raise ErrorMethod("Invalid Rubika login code")
    elif not platforms or numberphone or codehash or phone_code:
        raise ErrorMethod("Enter the complete values ​​into the method")


class Robot_Rubika(Messenger): ...
