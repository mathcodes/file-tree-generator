def format_tree(tree, indent_char='│   ', last_indent_char='└── ', empty_indent_char='    '):
    lines = tree.split('\n')
    formatted_tree = ''
    last_indents = []

    for line in lines:
        if line:
            indents = line.count('    ')
            current_indent = ''
            if indents > 0:
                current_indent += indent_char * (indents - 1)
                if indents != 1:
                    current_indent += last_indent_char
                else:
                    current_indent += empty_indent_char
            formatted_line = current_indent + line.strip()
            formatted_tree += formatted_line + '\n'
            last_indents = [current_indent]
        else:
            if last_indents:
                formatted_tree = formatted_tree.strip()
                for indent in last_indents[:-1]:
                    formatted_line = indent + last_indent_char
                    formatted_tree += formatted_line + '\n'

    return formatted_tree.strip()


powershell_output = '''
public
    _headers
    favicon.ico
    favicon.svg
    robots.txt
src
    assets
        images
            caos.jpg
            colors.jpg
            creativity.jpg
            default.png
            do-more.jpg
            hero.png
            stickers.jpg
            tools.jpg
            vintage.jpg
        styles
            base.css
    components
        blog
            Grid.astro
            GridItem.astro
            Headline.astro
            HighlightedPosts.astro
            LatestPosts.astro
            List.astro
            ListItem.astro
            Pagination.astro
            SinglePost.astro
            Tags.astro
            ToBlogLink.astro
        common
            BasicScripts.astro
            MetaTags.astro
            SocialShare.astro
            SplitbeeAnalytics.astro
            ToggleMenu.astro
            ToggleTheme.astro
        widgets
            Announcement.astro
            CallToAction.astro
            Content.astro
            FAQs.astro
            Features.astro
            Features2.astro
            Footer.astro
            Header.astro
            Hero.astro
            Hero2.astro
            Note.astro
            Stats.astro
            Steps.astro
            Steps2.astro
        CustomStyles.astro
        Logo.astro
    content
        post
            astrowind-template-in-depth.md
            get-started-website-with-astro-tailwind-css.md
            how-to-customize-astrowind-to-your-brand.md
            markdown-elements-demo-post.mdx
            useful-resources-to-create-websites.md
        config.ts
    layouts
        BaseLayout.astro
        MarkdownLayout.astro
        PageLayout.astro
    pages
        [...blog]
        landing
            mobile-app.astro
            saas.astro
            startup.astro
        404.astro
        index.astro
        privacy.md
        rss.xml.ts
        terms.md
    utils
        blog.ts
        directories.ts
        frontmatter.mjs
        images.ts
        permalinks.ts
        utils.ts
    config.mjs
    data.js
    env.d.ts
    types.ts
'''

formatted_tree = format_tree(powershell_output)
print(formatted_tree)
