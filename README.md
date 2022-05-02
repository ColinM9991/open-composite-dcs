# OvGME Packager for OpenXR – OpenComposite for DCS

## Note

This repository is now archived as the OpenXR changes have been merged with the OpenComposite upstream repository which uses a release process that isn't easily supported by this repository.

It is therefore recommended that you download the *System-wide installation* binary from the [upstream repository](https://gitlab.com/znixian/OpenOVR) as this will handle automatic updates and allow you to toggle between OpenXR and SteamVR globally.

## Description

This repository does not contain any of the code for the OpenCompositeACC project, nor is it affiliated in any way.  
I have created this simply to automate the process of packaging an OvGME-ready archive so it's easier to get up and running. Also within this archive is an updated version of the `opencomposite.ini` config file which includes the following additions
```ini
forceConnectedTouch=disabled
renderCustomHands=disabled
```

I highly recommend that you check out the following links, the DCS forum thread is a really good starting point.

[DCS Forum - OpenXR OpenComposite for DCS](https://forum.dcs.world/topic/295123-update-243-v061-openxr-quickstart-guide-for-g2-g1-and-other-headsets/)

[GitLab - OpenCompositeACC](https://gitlab.com/Jabbah/open-composite-acc/-/tree/MiniCompositor)

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
