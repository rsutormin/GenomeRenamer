
package us.kbase.genomerenamer;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: RenameGenomeParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "genome_ref",
    "new_genome_name"
})
public class RenameGenomeParams {

    @JsonProperty("genome_ref")
    private String genomeRef;
    @JsonProperty("new_genome_name")
    private String newGenomeName;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("genome_ref")
    public String getGenomeRef() {
        return genomeRef;
    }

    @JsonProperty("genome_ref")
    public void setGenomeRef(String genomeRef) {
        this.genomeRef = genomeRef;
    }

    public RenameGenomeParams withGenomeRef(String genomeRef) {
        this.genomeRef = genomeRef;
        return this;
    }

    @JsonProperty("new_genome_name")
    public String getNewGenomeName() {
        return newGenomeName;
    }

    @JsonProperty("new_genome_name")
    public void setNewGenomeName(String newGenomeName) {
        this.newGenomeName = newGenomeName;
    }

    public RenameGenomeParams withNewGenomeName(String newGenomeName) {
        this.newGenomeName = newGenomeName;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((("RenameGenomeParams"+" [genomeRef=")+ genomeRef)+", newGenomeName=")+ newGenomeName)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
