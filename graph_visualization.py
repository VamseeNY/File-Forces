import streamlit as st
import streamlit.components.v1 as components
import json

def create_force_directed_graph(data_json):
    """
    Create a D3.js force-directed graph visualization in Streamlit.
    
    Args:
        data_json (str): JSON string with directory structure data
    """
    # Create custom HTML with D3.js for the visualization
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <script src="https://d3js.org/d3.v7.min.js"></script>
        <style>
            #graph-container {{
                width: 100%;
                height: 600px;
                border: 1px solid #444;
                border-radius: 5px;
                overflow: hidden;
                margin-top: 10px;
                background-color: #1e1e1e;
            }}
            
            .node {{
                cursor: pointer;
            }}
            
            .node text {{
                font-family: sans-serif;
                font-size: 12px;
                text-anchor: middle;
                pointer-events: none;
                fill: #e0e0e0;
            }}
            
            .node circle {{
                stroke: #2d2d2d;
                stroke-width: 1.5px;
            }}
            
            .link {{
                fill: none;
                stroke: #656565;
                stroke-opacity: 0.6;
                stroke-width: 1.5px;
            }}
            
            .tooltip {{
                position: absolute;
                background: #2d2d2d;
                color: #e0e0e0;
                border: 1px solid #444;
                border-radius: 4px;
                padding: 10px;
                font-size: 12px;
                pointer-events: none;
                opacity: 0;
                transition: opacity 0.3s;
                box-shadow: 0 2px 4px rgba(0,0,0,0.3);
                max-width: 300px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }}
            
            .tooltip-title {{
                font-weight: bold;
                margin-bottom: 5px;
                color: #fff;
            }}
            
            .control-panel {{
                padding: 10px;
                background: #2d2d2d;
                border-bottom: 1px solid #444;
                display: flex;
                justify-content: space-between;
                color: #e0e0e0;
            }}
            
            #reset-zoom {{
                background-color: #383838;
                color: #e0e0e0;
                border: 1px solid #555;
                border-radius: 4px;
                padding: 5px 10px;
                cursor: pointer;
            }}
            
            #reset-zoom:hover {{
                background-color: #444;
            }}
            
            #link-strength {{
                background: #383838;
                border: 1px solid #555;
                height: 5px;
                border-radius: 2px;
            }}
            
            #link-strength::-webkit-slider-thumb {{
                background: #666;
                border: 1px solid #777;
            }}
            
            .progress-container {{
                width: 100%;
                background-color: #2d2d2d;
                border-radius: 4px;
                margin: 10px 0;
                overflow: hidden;
                display: none;
            }}
            
            .progress-bar {{
                height: 10px;
                background-color: #4CAF50;
                width: 0%;
                transition: width 0.3s;
            }}
        </style>
    </head>
    <body>
        <div class="control-panel">
            <div>
                <button id="reset-zoom">Reset View</button>
                <span style="margin-left: 15px; font-size: 12px;">
                    🔴 Files &nbsp; 🔵 Folders
                </span>
            </div>
            <div>
                <label for="link-strength">Link Strength:</label>
                <input type="range" id="link-strength" min="0.1" max="1" step="0.1" value="0.5">
            </div>
        </div>
        <div class="progress-container" id="progress-container">
            <div class="progress-bar" id="progress-bar"></div>
        </div>
        <div id="graph-container"></div>
        <div class="tooltip" id="tooltip"></div>
        <script>
            // Parse the data passed from Python
            const hierarchyData = {data_json};
            
            // Prepare the data for D3.js force-directed graph
            function prepareGraphData(data) {{
                const nodes = [];
                const links = [];
                
                function processNode(node, parentId = null) {{
                    const nodeId = nodes.length;
                    
                    // Add the current node
                    nodes.push({{
                        id: nodeId,
                        name: node.name,
                        path: node.path,
                        type: node.type,
                        extension: node.extension || "",
                        size: node.size || 0,
                        modified: node.modified || 0,
                        error: node.error || null
                    }});
                    
                    // Link to parent if exists
                    if (parentId !== null) {{
                        links.push({{
                            source: parentId,
                            target: nodeId
                        }});
                    }}
                    
                    // Process children recursively
                    if (node.children && node.children.length > 0) {{
                        for (const child of node.children) {{
                            processNode(child, nodeId);
                        }}
                    }}
                    
                    return nodeId;
                }}
                
                processNode(data);
                return {{ nodes, links }};
            }}
            
            // Show progress bar while processing data
            const progressContainer = document.getElementById("progress-container");
            const progressBar = document.getElementById("progress-bar");
            
            // Show the progress bar
            progressContainer.style.display = "block";
            progressBar.style.width = "25%";
            
            // Process data with simulated progress updates
            setTimeout(() => {{ progressBar.style.width = "50%"; }}, 200);
            setTimeout(() => {{ progressBar.style.width = "75%"; }}, 400);
            
            // Prepare graph data with a slight delay to show progress
            let graphData;
            setTimeout(() => {{
                graphData = prepareGraphData(hierarchyData);
                progressBar.style.width = "100%";
                
                // Hide progress bar after a short delay
                setTimeout(() => {{
                    progressContainer.style.display = "none";
                    // Create the visualization once data is prepared
                    createForceGraph();
                }}, 300);
            }}, 600);
            
            // Create the D3.js visualization
            function createForceGraph() {{
                // Clear any existing content
                d3.select("#graph-container").html("");
                
                // Create SVG container
                const containerWidth = document.getElementById("graph-container").clientWidth;
                const containerHeight = document.getElementById("graph-container").clientHeight;
                
                const svg = d3.select("#graph-container")
                    .append("svg")
                    .attr("width", containerWidth)
                    .attr("height", containerHeight);
                
                // Add zoom behavior
                const g = svg.append("g");
                
                const zoom = d3.zoom()
                    .scaleExtent([0.1, 8])
                    .on("zoom", (event) => {{
                        g.attr("transform", event.transform);
                    }});
                
                svg.call(zoom);
                
                // Reset zoom button functionality
                d3.select("#reset-zoom").on("click", () => {{
                    svg.transition()
                        .duration(750)
                        .call(zoom.transform, d3.zoomIdentity);
                }});
                
                // Create tooltip
                const tooltip = d3.select("#tooltip");
                
                // Get link strength from slider
                let linkStrength = parseFloat(document.getElementById("link-strength").value);
                
                // Update force simulation when slider changes
                d3.select("#link-strength").on("input", function() {{
                    linkStrength = parseFloat(this.value);
                    simulation.force("link").strength(linkStrength);
                    simulation.alpha(0.3).restart();
                }});
                
                // Create the simulation
                const simulation = d3.forceSimulation(graphData.nodes)
                    .force("link", d3.forceLink(graphData.links)
                        .id(d => d.id)
                        .distance(50)
                        .strength(linkStrength))
                    .force("charge", d3.forceManyBody().strength(-100))
                    .force("center", d3.forceCenter(containerWidth / 2, containerHeight / 2))
                    .force("x", d3.forceX(containerWidth / 2).strength(0.05))
                    .force("y", d3.forceY(containerHeight / 2).strength(0.05));
                
                // Draw links
                const link = g.append("g")
                    .attr("class", "links")
                    .selectAll("line")
                    .data(graphData.links)
                    .enter()
                    .append("line")
                    .attr("class", "link");
                
                // Draw nodes
                const node = g.append("g")
                    .attr("class", "nodes")
                    .selectAll(".node")
                    .data(graphData.nodes)
                    .enter()
                    .append("g")
                    .attr("class", "node")
                    .call(d3.drag()
                        .on("start", dragstarted)
                        .on("drag", dragged)
                        .on("end", dragended));
                
                // Add circles to node groups
                node.append("circle")
                    .attr("r", d => d.type === "folder" ? 8 : 5)
                    .attr("fill", d => getNodeColor(d))
                    .on("mouseover", showTooltip)
                    .on("mouseout", hideTooltip)
                    .on("click", highlightConnections);
                
                // Add text labels to nodes
                node.append("text")
                    .attr("dy", 15)
                    .text(d => truncateText(d.name, 20));
                
                // Function to truncate text with ellipsis
                function truncateText(text, maxLength) {{
                    return text.length > maxLength ? text.substring(0, maxLength) + "..." : text;
                }}
                
                // Get node color based on type and extension
                function getNodeColor(node) {{
                    if (node.error) {{
                        return "#ff6666"; // Red for error
                    }}
                    
                    if (node.type === "folder") {{
                        return "#4285F4"; // Blue for folders
                    }}
                    
                    // For files, color by extension category
                    const ext = node.extension.toLowerCase();
                    if (['.js', '.py', '.java', '.c', '.cpp', '.html', '.css', '.php', '.swift', '.go'].includes(ext)) {{
                        return "#DB4437"; // Code files
                    }} else if (['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.md'].includes(ext)) {{
                        return "#F4B400"; // Document files
                    }} else if (['.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp', '.webp'].includes(ext)) {{
                        return "#0F9D58"; // Image files
                    }} else {{
                        return "#E91E63"; // Other files
                    }}
                }}
                
                // Show tooltip with node details
                function showTooltip(event, d) {{
                    let tooltipContent = `
                        <div class="tooltip-title">${{d.name}}</div>
                        <div>Type: ${{d.type === "folder" ? "Folder" : "File"}}</div>
                        <div>Path: ${{d.path}}</div>
                    `;
                    
                    if (d.type === "file") {{
                        tooltipContent += `
                            <div>Extension: ${{d.extension || "None"}}</div>
                            <div>Size: ${{formatBytes(d.size)}}</div>
                            <div>Modified: ${{formatDate(d.modified)}}</div>
                        `;
                    }}
                    
                    if (d.error) {{
                        tooltipContent += `<div style="color: red">Error: ${{d.error}}</div>`;
                    }}
                    
                    tooltip.html(tooltipContent)
                        .style("left", (event.pageX + 10) + "px")
                        .style("top", (event.pageY - 10) + "px")
                        .style("opacity", 1);
                }}
                
                // Hide tooltip
                function hideTooltip() {{
                    tooltip.style("opacity", 0);
                }}
                
                // Highlight connections on click
                function highlightConnections(event, d) {{
                    // Reset all links and nodes
                    link.style("stroke", "#656565").style("stroke-width", 1.5);
                    node.select("circle").style("stroke", "#2d2d2d").style("stroke-width", 1.5);
                    
                    // Find connected links and nodes
                    const connectedLinks = graphData.links.filter(l => 
                        l.source.id === d.id || l.target.id === d.id
                    );
                    
                    const connectedNodeIds = new Set();
                    connectedLinks.forEach(l => {{
                        connectedNodeIds.add(l.source.id);
                        connectedNodeIds.add(l.target.id);
                    }});
                    
                    // Highlight connected links
                    link.filter(l => l.source.id === d.id || l.target.id === d.id)
                        .style("stroke", "#ff7f0e")
                        .style("stroke-width", 3);
                    
                    // Highlight connected nodes
                    node.filter(n => connectedNodeIds.has(n.id))
                        .select("circle")
                        .style("stroke", "#ff7f0e")
                        .style("stroke-width", 3);
                    
                    // Stop event propagation
                    event.stopPropagation();
                }}
                
                // Reset highlights when clicking on background
                svg.on("click", () => {{
                    link.style("stroke", "#656565").style("stroke-width", 1.5);
                    node.select("circle").style("stroke", "#2d2d2d").style("stroke-width", 1.5);
                }});
                
                // Format bytes to human-readable format
                function formatBytes(bytes) {{
                    if (!bytes || isNaN(bytes) || bytes === 0) return "0 B";
                    const sizes = ["B", "KB", "MB", "GB", "TB"];
                    const i = Math.floor(Math.log(bytes) / Math.log(1024));
                    return parseFloat((bytes / Math.pow(1024, i)).toFixed(2)) + " " + sizes[i];
                }}
                
                // Format timestamp to readable date
                function formatDate(timestamp) {{
                    if (!timestamp) return "Unknown";
                    return new Date(timestamp * 1000).toLocaleString();
                }}
                
                // Drag functions
                function dragstarted(event, d) {{
                    if (!event.active) simulation.alphaTarget(0.3).restart();
                    d.fx = d.x;
                    d.fy = d.y;
                }}
                
                function dragged(event, d) {{
                    d.fx = event.x;
                    d.fy = event.y;
                }}
                
                function dragended(event, d) {{
                    if (!event.active) simulation.alphaTarget(0);
                    d.fx = null;
                    d.fy = null;
                }}
                
                // Update simulation on tick
                simulation.on("tick", () => {{
                    link
                        .attr("x1", d => d.source.x)
                        .attr("y1", d => d.source.y)
                        .attr("x2", d => d.target.x)
                        .attr("y2", d => d.target.y);
                    
                    node.attr("transform", d => `translate(${{d.x}},${{d.y}})`);
                }});
            }}
            
            // Initialize the visualization
            createForceGraph();
            
            // Handle window resize
            window.addEventListener("resize", () => {{
                createForceGraph();
            }});
        </script>
    </body>
    </html>
    """
    
    # Display the HTML in Streamlit
    components.html(html_code, height=680)
