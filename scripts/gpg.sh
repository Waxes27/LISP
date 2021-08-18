gpg --full-generate-key
gpg --list-secret-keys --keyid-format=long
gpg --armor --export {{sec stuff after /}}
git config --global user.signingkey {{sec stuff after /}}

