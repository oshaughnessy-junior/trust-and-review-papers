# Put the candidate on publication surfaces without changing its meaning

Prepared integration plan for the existing outward-facing Jekyll research site.
No site file, public repository, deployment setting or external account was changed
by this packet. Paths below are proposed placements, not existing public URLs.

## Recommended split

Use the existing site for the introductory post and a link to the versioned
research object. Serve the complete reading/code export as a plain static artifact
or downloadable ZIP. Keep its source and result manifest alongside it. A separate
static export repository, if approved, should contain only the curated export,
not the private research repository's Git history.

The candidate builder includes `.nojekyll` for a **standalone static export root**.
Do not copy that file to the existing Jekyll site's root: doing so would change
how that whole site builds. The marker is a hosting hint, not an integrity proof;
the chosen deployment route still needs an actual retrieval check.

A full export contains Markdown sources, including front matter. Copying all of
those sources into a Jekyll tree and assuming they will be served unchanged is
unsafe: the site generator can interpret source files or create competing rendered
paths. Either serve the curated export without that transformation, or publish
its ZIP and PDF as static downloads while intentionally integrating the blog.
The download is the canonical self-contained reproduction object.

## Prepare the site post

The editorial source is [blog-introduction.md](blog-introduction.md). Its front
matter includes the current site's `layout`, `categories`, `publication_lane`,
AI disclosure and related-post conventions, with **`published: false`**. It is
ready for a draft integration, not an authorization to turn that flag on.

A proposed filename is `_drafts/mcrp-what-can-we-rely-on.md`. On a later approved
publication, choose the actual date and `_posts/YYYY-MM-DD-...md` filename. The
site's layout supplies the visible title, so remove the source's duplicate H1
when adapting it. Preserve the contribution disclosure and distinction between
internal agent review and external human review.

Resolve all relative links against the **selected public export**, including these entry points:

| Link in editorial source | Artifact entry |
|---|---|
| Human exercise | `onboarding/human-path.html` |
| Implementer quickstart | `onboarding/agent-path.html` |
| Domain cases | `domains/README.html` |
| Collective critique | `reviews/COLLECTIVE.html` |
| Positioning comparison | `publication/positioning-and-adoption.html` |

Do not invent a working destination or DOI before one exists. A draft can retain
clearly labeled unresolved destinations; the publication candidate cannot. If the
initial surface provides only a ZIP, make the download the entry and explain that
`index.html` is its local starting page. Do not publish relative links that happen
to work only in the authoring checkout.

## Exact release sequence

1. Select the responsible attribution, rights disposition, destination and feedback
   owner for a specific source and export inventory. The recommendation remains
   public release of a research seed, with the declared synthetic evidence limits.
2. Build and inspect the post in the site's own toolchain. Check navigation,
   intended links, contribution disclosure, mobile layout and dark mode. The
   standalone packet's browser checks do not substitute for this integration check.
3. Record the final site-post bytes, exported ZIP digest and public path mapping.
   Site layout changes can alter the rendered post; bind the approval to the
   rendered candidate as well as the editorial source.
4. Publish only within the approved scope. Retrieve the public ZIP and manifest,
   compare them with the approved local bytes, and inspect the actual public post.
   A successful build or deployment command is not evidence of successful delivery.
5. Record a dated observation. Later source changes require a new version and a
   new decision for the affected public artifact. Keep old versions identifiable;
   never silently replace a DOI or download label with different evidence.

These steps make the proposed launch concrete. The current task prepares the
candidate and its evidence; it does not claim that an external page was deployed
or observed. A next publication instruction can name the exact destination and
byline rather than reopen the research design.
