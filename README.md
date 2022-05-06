# OvGME Packager for OpenXR – OpenComposite for DCS

## Note

This repository is currently unsupported and needs to be migrated to the upstream OpenComposite repository.

I've had issues with toggling between SteamVR and OpenComposite using the OpenComposite Runtime Switcher (global installer) and have decided to maintain the OvGME repository as a way of running OpenComposite on DCS while using SteamVR for all other games, such as Onward.

An update will arrive over the coming days to reintroduce automated releases on a commit basis from the upstream OpenComposite repository.

## Description

This repository does not contain any of the code for the OpenCompositeACC project, nor is it affiliated in any way.  
I have created this simply to automate the process of packaging an OvGME-ready archive so it's easier to get up and running. Also within this archive is an updated version of the `opencomposite.ini` config file which includes the following additions
```ini
forceConnectedTouch=disabled
renderCustomHands=disabled
```

I highly recommend that you check out the following links, the DCS forum thread is a really good starting point.

[DCS Forum - OpenXR OpenComposite for DCS](https://forum.dcs.world/topic/295123-update-243-v061-openxr-quickstart-guide-for-g2-g1-and-other-headsets/)

[GitLab - OpenComposite](https://gitlab.com/znixian/OpenOVR/-/tree/openxr)

## Usage

### Prerequisites

To use this you'll first need [OvGME](https://wiki.hoggitworld.com/view/OVGME).

**Do not** use your user profile `Downloads` folder as the OvGME repository. You know who you are.

### Importing

The archive comes prepacked with a Version file so OvGME can differentiate between versions.

Assuming you have correctly cofigured OvGME, the simplest way to set this up is:

1. View the [latest releases](https://github.com/ColinM9991/open-composite-dcs/releases)
2. Download the `OCXR_WMR_APP.zip` archive
3. Open OvGME
4. Click `Import Mods`
5. Choose the newly downloaded `OCXR_WMR_APP.zip` archive
6. Activate the mod

## Credit

It's pretty obvious who credit goes to (see the above links). All I've done is automate the process of creating OvGME ready archives, basically none of the hard work of developing and investigating the use case for DCS.
