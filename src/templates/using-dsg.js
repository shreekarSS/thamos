import React from "react"
import { Helmet } from "react-helmet"
import { graphql } from "gatsby"

// import '../css/blog-post.css'; // make it pretty!
export default function Template({
	data // this prop will be injected by the GraphQL query we'll write in a bit
}) {
	const {markdownRemark: post} = data;// data.markdownRemark holds your post data
	return (
	    <div dangerouslySetInnerHTML={{ __html: post.html}} />
	    );
}

export const pageQuery = graphql`
  query BlogPostByPath($path: String!) {
    markdownRemark(frontmatter: { id:{ eq: $id }  }) {
      html
      }
    }
`
