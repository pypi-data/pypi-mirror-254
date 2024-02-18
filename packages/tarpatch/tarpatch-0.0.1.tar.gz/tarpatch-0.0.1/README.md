# TarPatch

Binary patches for tarballs

>BEWARE: THIS PROJECT IS STILL IN THE EXPERIMENTAL PHASE

### What is tarpatch?

Tarpatch allows you to create a patch that represents the difference between two tar archives (a.k.a. tarballs).

This patch is typically much smaller than the archives themselves, so it can be used for efficient transmission of updates.

Instead of creating a single monolithic binary diff, tarpatch creates binary diffs for the individual files in the archives.

The resulting patch file can be inspected easily, because it is in JSON format.

### FAQ

- Q: Why not simply create a monolithic binary difference file using e.g. `bsdiff`?
  A: For small archives, something like [`bsdiff`][10] would probably be a better choice. 
     However, as archives grow larger, using `bsdiff` can become too expensive in terms of [memory use][10].  

### Questions?

Please have a look at the [Q&A][1] and existing [issues][2].

### Similar or related projects

- [bsdiff4][3] (Python)
- [Courgette][8] from Chromium (C++, [source][9])
- [containers/tar-diff][4] (Go)
- [difflib][5] (Python, standard library)
- [GNU diffutils][6]
- [GNU patch][7]

[1]: https://github.com/dennisvang/tarpatch/discussions/categories/q-a
[2]: https://github.com/dennisvang/tarpatch/issues
[3]: https://github.com/ilanschnell/bsdiff4
[4]: https://github.com/containers/tar-diff
[5]: https://docs.python.org/3/library/difflib.html
[6]: https://www.gnu.org/software/diffutils/
[7]: https://savannah.gnu.org/projects/patch/
[8]: https://www.chromium.org/developers/design-documents/software-updates-courgette/
[9]: https://chromium.googlesource.com/chromium/src/courgette/+/HEAD
[10]: https://www.daemonology.net/bsdiff/
